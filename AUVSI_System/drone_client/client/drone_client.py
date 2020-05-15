"""Core drone client module

This module provides a Python interface to the drone using mavsdk.
"""
import asyncio
import json

from auvsi_suas.client.exceptions import InteropError
from auvsi_suas.proto import interop_api_pb2
from concurrent.futures import ThreadPoolExecutor
from auvsi_suas.client.client import AsyncClient
from mavsdk import System
from mavsdk import (MissionItem, MissionPlan)

class DroneClient():
    def __init__(self, url):
        self.drone = System()
        self.url = url

    async def connect(self):
        await self.drone.connect(system_address=self.url)

        print("Waiting for drone to connect...")
        async for state in self.drone.core.connection_state():
            if state.is_connected:
                print(f"Drone discovered with UUID: {state.uuid}")
                break    

    async def load_mission(self, mission_id, interop_client_bridge):
        """get mission from the interop server and send it to drone."""
        await self.connect()

        mission = interop_client_bridge.get_mission(mission_id)
        mission_dictionary = json.loads(mission)

        mission_items = []
        mission_items.append(MissionItem(38.1446916666667,
                                        -76.4279944444445,
                                        25,
                                        10,
                                        True,
                                        float('nan'),
                                        float('nan'),
                                        MissionItem.CameraAction.NONE,
                                        float('nan'),
                                        float('nan')))
        for waypoint in mission_dictionary['waypoints']:
            mission_items.append(MissionItem(waypoint['latitude'],
                                             waypoint['longitude'],
                                             waypoint['altitude'],
                                             10,
                                             True,
                                             float('nan'),
                                             float('nan'),
                                             MissionItem.CameraAction.NONE,
                                             float('nan'),
                                             float('nan')))
    
        await self.drone.mission.set_return_to_launch_after_mission(True)

        mission_plan = MissionPlan(mission_items)

        print("-- Uploading mission")
        await self.drone.mission.upload_mission(mission_plan)

    async def start_mission(self):
        """run a mission that was sent by load_mission."""
        termination_task = asyncio.ensure_future(self.observe_is_in_air())

        await self.connect()

        print("-- Arming")
        await self.drone.action.arm()

        print("-- Starting mission")
        await self.drone.mission.start_mission()

        await termination_task

    async def mission(self):
        """test to see if drone mission works"""
        await self.connect()

        asyncio.ensure_future(self.print_mission_progress())
        termination_task = asyncio.ensure_future(self.observe_is_in_air())

        mission_items = []
        mission_items.append(MissionItem(38.1446916666667,
                                        -76.4279944444445,
                                        25,
                                        10,
                                        True,
                                        float('nan'),
                                        float('nan'),
                                        MissionItem.CameraAction.NONE,
                                        float('nan'),
                                        float('nan')))

        await self.drone.mission.set_return_to_launch_after_mission(True)

        print("-- Uploading mission")
        await self.drone.mission.upload_mission(mission_items)

        print("-- Arming")
        await self.drone.action.arm()

        print("-- Starting mission")
        await self.drone.mission.start_mission()

        await termination_task


    async def print_mission_progress(self):
        async for mission_progress in self.drone.mission.mission_progress():
            print(f"Mission progress: "
                f"{mission_progress.current_item_index}/"
                f"{mission_progress.mission_count}")


    async def observe_is_in_air(self):
        """ Monitors whether the drone is flying or not and
        returns after landing """

        was_in_air = False

        async for is_in_air in self.drone.telemetry.in_air():
            if is_in_air:
                was_in_air = is_in_air

            if was_in_air and not is_in_air:
                await asyncio.get_event_loop().shutdown_asyncgens()
                return
