FROM auvsisuas/interop-client
WORKDIR /interop/client
COPY drone_client/ ./drone_client/
COPY tools/interop_cli.py ./tools/interop_cli.py
COPY tools/drone_cli.py ./tools/drone_cli.py
COPY requirements37.txt ./requirements37.txt 

RUN apt-get update && apt-get install -y vim 

RUN apt-get -qq update && apt-get -qq install -y \
        python3.7 \
        python3.7-dev 

RUN bash -c "cd /interop/client && \
        virtualenv --system-site-packages -p /usr/bin/python3.7 venv37 && \
        source venv37/bin/activate && \
        pip install -r requirements37.txt && \
        deactivate"
