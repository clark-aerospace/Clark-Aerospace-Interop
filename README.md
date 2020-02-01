# AUVSI_System
This system is a ground control application. It can comunicates with a mavlink enabled drone and the AUVSI interop server. 

## getting started

install django
```
python -m pip install Django
```
install jsonify
```
pip install jsonify
```
run ground control django web app
```
cd Clark-Aerospace-Interop/AUVSI_SYSTEM
./my_client.sh run
```

## Instructions on how to establish connections between mavproxy, QGround control, Gazebo, PX4, the AUVSI interop server, and this Django interop client for testing

### These isntructions assume that you have succesfully installed all dependencies. If it is requested I can add more instruction.

navigate to the AUVSI interop server directory
```bash
cd interop/server
```
start the interop test server
```bash
./interop-server.sh up
```
set home coordinates to event location<br>
and run px4 with gazebo using the default vtol model
```bash
export PX4_HOME_LAT=38.1446916666667
export PX4_HOME_LON=-76.4279944444445
export PX4_HOME_ALT=28.0
make px4_sitl gazebo_standard_vtol
```
Use mavproxy to split the mavlink signal into two streams on ports 14550 and 14551.
```bash
mavproxy.py --master=udp:127.0.0.1:14550 --out=udp:127.0.0.1:14550 --out=udp:127.0.0.1:14551 
```
run QGround control
```bash
./Downloads/QGroundControl.AppImage
```
navigate to the Clark-Aerospace-Interop directory and build and run our custom interop client.
```bash
cd Document/Clark-Aeropspace-Interop/AUVSI_System 
./my_client.sh run
```