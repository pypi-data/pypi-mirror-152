#!/bin/bash

OS_VERSION=$( . /etc/os-release ; echo $VERSION_ID)
echo "System OS : $OS_VERSION"

if [[ $OS_VERSION != "18.04" ]]; then
        echo "The application only supports Ubuntu18 OS. Please select the specified OS for the application"
        echo "Exiting the MarketPlace component installation....."
        exit 1

fi

echo "Installing cargo-management ..."
pip3 install --upgrade pip --user && pip3 install edgesoftware --user
echo 548eba24-4079-47cb-8d89-db324668e301 | $HOME/.local/bin/edgesoftware install cargo-management 61bc6972d8ecccee555fb963
