#!/bin/bash

OS_VERSION=$( . /etc/os-release ; echo $VERSION_ID)
echo "System OS : $OS_VERSION"

if [[ $OS_VERSION != "18.04" ]]; then
        echo "The application only supports Ubuntu18 OS. Please select the specified OS for the application"
        echo "Exiting the MarketPlace component installation....."
        exit 1

fi

echo "Installing drive-behavior-analytics ..."
pip3 install --upgrade pip --user && pip3 install edgesoftware --user
echo 35aaed01-8674-44ed-a865-834183abff3c | $HOME/.local/bin/edgesoftware install drive-behavior-analytics 61bc69a8d8ecccee555fc0fa

