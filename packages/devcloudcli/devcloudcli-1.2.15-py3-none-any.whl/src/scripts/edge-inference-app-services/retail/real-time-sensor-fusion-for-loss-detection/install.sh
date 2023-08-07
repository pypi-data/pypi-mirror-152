#!/bin/bash

OS_VERSION=$( . /etc/os-release ; echo $VERSION_ID)
echo "System OS : $OS_VERSION"

if [[ $OS_VERSION != "18.04" ]]; then
        echo "The application only supports Ubuntu18 OS. Please select the specified OS for the application"
        echo "Exiting the MarketPlace component installation....."
        exit 1

fi

echo "Installing retail-real-time-sensor-fusion-for-loss-detection ..."
pip3 install --upgrade pip --user && pip3 install edgesoftware --user
echo 8ecf6818-1c42-40bf-a5c5-2d0043575ffb | $HOME/.local/bin/edgesoftware install retail-real-time-sensor-fusion-for-loss-detection 61712992d8ecccee5521c566

