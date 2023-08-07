#!/bin/bash
# Copyright (C) 2018-2021 Intel Corporation
# SPDX-License-Identifier: Apache-2.0

echo $1
if [ "$(echo "intel123" | sudo docker ps -q -f name=$1)" ]; then
    echo "Restarting $1 service"
    export HOST_IP=$(hostname -I | cut -d' ' -f1)
    if [ $1=="all-services" ]; then      
        sudo -E docker-compose -f $PWD/devcloud/docker-compose-app-service.yaml restart $1
         grafana influxdb collectd
    fi
fi


