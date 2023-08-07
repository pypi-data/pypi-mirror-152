#!/bin/bash
# Copyright (C) 2018-2021 Intel Corporation
# SPDX-License-Identifier: Apache-2.0

echo $1
if [ "$(echo "intel123" | sudo docker ps -q -f name=^influxdb$)" ]; then
    echo "Installing Telemetry service"
    export HOST_IP=$(hostname -I | cut -d' ' -f1)
    if [ $1=="all-services" ]; then        
        sudo -E docker-compose -f $PWD/docker-compose-app-service.yaml stop influxdb grafana collectd
	sudo docker rm -f $(sudo docker ps -aq)
    else
        sudo -E docker-compose -f $PWD/docker-compose-app-service.yaml stop $1
    fi
else
    echo "Telemetry is not running"
    echo -e "To start run command: '\e[1;3;4;33meval app-services telemetry start $1\e[0m'"
fi
