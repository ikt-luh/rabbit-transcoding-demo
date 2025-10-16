# SPIRIT Demo

This repository is part of the implementation for the SPIRIT project **RABBIT@Scale**.

The overall project structure is the following:
TODO

## Description
The structure of this repository is as follows:
TODO

It contains code for the demo shown at the EuroXR conference 2025.
The Demo runs a transcoding service and a client, where the client requests and renders segments of a point cloud stream.
The transcoding service performs on-the-fly transcoding of the requested segments. 

Note that we require a implementation of the tmc2-rs decoder to run the demo. 
A branch of the original repo with additional python bindings for usage in this demo can be found [here](wherever).


## Setup
You can run the demo locally on 1 device or on 2 devices on the same network.

### Single-Device setup
```
  docker compose -f docker-compose.demo.yaml up --build
```

### Two-Device setup
f you want to run on 2 devices, make sure they are connected via ethernet and Port 8000 is opened on the server side device. Then, change the IP-Address in docker-compose.demo-client.yaml to the IP of the server.

On the server, start the transcoder with
```
  docker compose -f docker-compose.demo-server.yaml up --build
```

and on the client, run
```
  docker compose -f docker-compose.demo-client.yaml up --build
```

## Usage
How to create a new experiment

