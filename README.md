# AUVSI_System
This system is a ground control application. It can comunicates with a mavlink enabled drone and the AUVSI interop server. 

# Getting Started

## **Install The Following Software**
#### this list is incomlete for now

install django with python3
```
python -m pip install Django
```
install jsonify
```
pip install jsonify
```

## **First Time Setup**

### set up python2 virual environments.
This is for executing the interop client.
```bash
virtualenv --system-site-packages -p /usr/bin/python2 venv2 && \
source venv2/bin/activate && \
pip install -r requirements.txt && \
deactivate
```
run setup.py in virtual environment venv2
```bash
cd /interop/client && \
source venv2/bin/activate && \
python setup.py install && \
deactivate
```

### Install auvsi_suas client library
The competition provides a client library to make integration easier. To run the drone_client system locally you must install this libary. You can install the client library by executing setup commands listed [here](https://github.com/auvsi-suas/interop/blob/master/client/Dockerfile).

You will also need to add the auvsi_suas python module to the python path variable. Add the following line to your `~/.bashrc` file.
```
export PYTHONPATH="${PYTHONPATH}:/home/treverhibbs/Documents/projects/Clark-Aerospace-Interop/AUVSI_System/client"
```

### setup the interop server
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
and run px4 with gazebo using the default vtol model<br>

First navigate to the PX4 Firmware directory.<br>
default Firmware directory path = /home/username/src
```bash
cd /home/username/src
export PX4_HOME_LAT=38.1446916666667
export PX4_HOME_LON=-76.4279944444445
export PX4_HOME_ALT=28.0
make px4_sitl gazebo_standard_vtol
```
If you want to have a faster simulation set the following variable to 20.
```bash
export PX_SIM_SPEED_FACTOR=20
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
view the test files to see what tests are available.<br>

## **Current Task**

Integrate drone_client class with django UI.

### Old Tasks

~~Create method for droneClient class that sends a mission item to the device.~~<br>
~~Create test class for cli bridge class~~ <br>
~~Update read me with get started instruction~~
