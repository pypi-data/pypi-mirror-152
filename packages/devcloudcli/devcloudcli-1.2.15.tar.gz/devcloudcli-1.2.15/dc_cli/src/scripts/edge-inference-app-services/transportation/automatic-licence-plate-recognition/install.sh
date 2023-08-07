#!/bin/bash

OS_VERSION=$( . /etc/os-release ; echo $VERSION_ID)
echo "System OS : $OS_VERSION"

if [[ $OS_VERSION != "18.04" ]]; then
        echo "The application only supports Ubuntu18 OS. Please select the specified OS for the application"
        echo "Exiting the MarketPlace component installation....."
        exit 1

fi

echo "Installing automatic-licence-plate-recognition ..."
pip3 install --upgrade pip --user && pip3 install edgesoftware --user
echo fe86f27f-7ec8-4550-a964-be67d3d895b5 | $HOME/.local/bin/edgesoftware install automatic-licence-plate-recognition 61f38cca14e68bcc9220ccb8
