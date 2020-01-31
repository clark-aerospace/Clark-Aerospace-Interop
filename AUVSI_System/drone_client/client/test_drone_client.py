import os
import unittest
import asyncio

from drone_client import DroneClient
from interop_cli_bridge import InteropCliBridge

# These tests run a SITL drone simulation using gazebo and default settings

# Set these environmental variables to the proper values
# if the defaults are not correct.
device = os.getenv('TEST_DRONE', 'udp://:14540')
interop_server = os.getenv('TEST_DRONE', 'http://127.0.0.1:8000')
interop_username = os.getenv('TEST_DRONE', 'testuser')
interop_password = os.getenv('TEST_DRONE', 'testpass')

class TestClientMission(unittest.TestCase):
    """Test if the mission function connects and sends mission items to device"""

    def test_mission(self):
        """send good mission on url"""
        #if no exeption is raised it works
        client = DroneClient(device)
        asyncio.run(client.mission())

    def test_load_mission(self):
        """send good mission using load_mission"""
        #if no exeption is raised it works
        client = DroneClient(device)
        interop_client_bridge = InteropCliBridge(interop_server,
                         interop_username,
                         interop_password)
        asyncio.run(client.load_mission(1, interop_client_bridge))

    def test_start_mission(self):
        """start mission after mission has been loaded."""
        client = DroneClient(device)
        asyncio.run(client.start_mission())
