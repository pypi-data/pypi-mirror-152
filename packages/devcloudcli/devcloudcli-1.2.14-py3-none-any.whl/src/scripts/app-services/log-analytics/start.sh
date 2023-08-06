#!/bin/bash
# Copyright (C) 2018-2021 Intel Corporation
# SPDX-License-Identifier: Apache-2.0

echo $1
if [ "$(echo "intel123" | sudo docker ps -q -f name=^loki$)" ]; then
    echo "Telemetry already running"
    echo -e "To stop run command: '\e[1;3;4;33meval app-services analytics stop \e[0m'"
else
    echo "Installing Telemetry service"
    export HOST_IP=$(hostname -I | cut -d' ' -f1)
    COMPOSE_PROFILES=native sudo -E docker-compose -f $PWD/docker-compose-app-service.yaml  up -d --build loki promtail grafana
    #sudo -E docker-compose -f $PWD/devcloud/docker-compose-app-services.yaml up -d --build loki promtail grafana      
    
fi



