# AUVSI_System
This system is a ground control application. It can comunicates with a mavlink enabled drone and the AUVSI interop server. 

# Getting Started

## **Install The Following Software**
#### this list is incomlete for now

install django
```
python -m pip install Django
```
install jsonify
```
pip install jsonify
```

## **First Time Setup**

Begin by setting up the interop client for testing.<br>
run setup.py script. This will configure the AUVSI server API.
```bash
cd AUVSI_System/client
python setup.py
```
create the python2 virtual environment.
This is for executing the interop client.
```bash
virtualenv --system-site-packages -p /usr/bin/python2 venv2 && \
source venv2/bin/activate && \
pip install -r requirements.txt && \
deactivate" && \
```
copy the proto directory to ../proto if not allready there.
```bash
mv proto ../proto
```
run setup.py in virtual environment venv2
```bash
cd /interop/client && \
source venv2/bin/activate && \
python setup.py install && \
deactivate"
```
navigate to the interop server directory <br>
build the docker image, the database, and <br>
load test data. 
```bash
cd interop/server
sudo ./interop-server.sh create_db
sudo ./interop-server.sh load_test_data
```

## **Running The Interop Client And Test Environment Software**
### These instructions assume that you have succesfully installed all dependencies. If it is requested I can add more instruction.

run ground control django web app
```
cd Clark-Aerospace-Interop/AUVSI_SYSTEM
./my_client.sh run
```
navigate to the AUVSI interop server directory and <br>
start the interop test server
```bash
cd interop/server
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
Everything should be set up let me know on discord if this helps or not. <br>
my discord -> Trever Hibbs #1463

## **Testing Guide**

I am using unittest to test functions and classes. <br>
The syntax for running a single test method is...
```bash
python -m unittest path.to.test_method.method 
```
view the test files to see what tests are available.

## **Current Task**

Create method for droneClient class that sends a mission item to the device.

### Old Tasks

~~Create test class for cli bridge class~~ <br>
~~Update read me with get started instruction~~