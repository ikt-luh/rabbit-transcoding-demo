FROM pyrabbit-transcoder-hw

WORKDIR /app
COPY ./src /app/src
COPY requirements.txt ./requirements.txt
RUN python3 -m pip install -r requirements.txt

ENTRYPOINT []
CMD ["python3", "/app/src/run_demo_server.py"]