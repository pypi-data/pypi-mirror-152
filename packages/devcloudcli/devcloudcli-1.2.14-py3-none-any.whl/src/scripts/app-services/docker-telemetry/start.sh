#!/bin/bash
# Copyright (C) 2018-2021 Intel Corporation
# SPDX-License-Identifier: Apache-2.0

echo $
if [ "$(echo "intel123" | sudo docker ps -q -f name=^influxdb$)" ]; then
    echo "Telemetry already running"
    echo -e "To stop run command: '\e[1;3;4;33meval app-services telemetry stop $1\e[0m'"
else
    echo "Installing Telemetry service"
    export HOST_IP=$(hostname -I | cut -d' ' -f1)
    if [ $1=="all-services" ]; then      
        COMPOSE_PROFILES=native sudo -E docker-compose -f $PWD/docker-compose-app-service.yaml  up -d --build influxdb grafana cadvisor prometheus    
    fi
fi
