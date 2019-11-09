FROM auvsisuas/interop-client
WORKDIR /interop/client
COPY hello.py ./
COPY drone_mission/ ./drone_mission/
COPY AUVSI_System/ ./AUVSI_System/
RUN apt-get update && apt-get install -y vim 
RUN apt-get update && apt-get install -y python3-django 
RUN apt-get update && pip3 install -U Django
