#!/bin/bash

OS_VERSION=$( . /etc/os-release ; echo $VERSION_ID)
echo "System OS : $OS_VERSION"

if [[ $OS_VERSION != "18.04" ]]; then
        echo "The application only supports Ubuntu18 OS. Please select the specified OS for the application"
        echo "Exiting the MarketPlace component installation....."
        exit 1

fi

echo "Installing workzone-analytics ..."
pip3 install --upgrade pip --user && pip3 install edgesoftware --user
echo 83603d3e-f16f-42dc-bfea-62aec06aaced | $HOME/.local/bin/edgesoftware install workzone-analytics 623d8ced9654a8f4bdb5ca20
