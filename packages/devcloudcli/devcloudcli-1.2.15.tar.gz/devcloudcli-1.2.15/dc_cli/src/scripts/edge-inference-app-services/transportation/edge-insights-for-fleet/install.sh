#!/bin/bash

OS_VERSION=$( . /etc/os-release ; echo $VERSION_ID)
echo "System OS : $OS_VERSION"

if [[ $OS_VERSION != "18.04" ]]; then
        echo "The application only supports Ubuntu18 OS. Please select the specified OS for the application"
        echo "Exiting the MarketPlace component installation....."
        exit 1

fi

echo "Installing edge-insights-for-fleet ..."
pip3 install --upgrade pip --user && pip3 install edgesoftware --user
echo ecac9ea2-9ba2-4996-aeda-9c60d9e213f0 | $HOME/.local/bin/edgesoftware install edge-insights-for-fleet 623c98c39654a8f4bd94fa4b
