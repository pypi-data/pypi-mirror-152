#!/bin/bash

OS_VERSION=$( . /etc/os-release ; echo $VERSION_ID)
echo "System OS : $OS_VERSION"

if [[ $OS_VERSION != "18.04" ]]; then
        echo "The application only supports Ubuntu18 OS. Please select the specified OS for the application"
        echo "Exiting the MarketPlace component installation....."
        exit 1

fi

echo "Installing automated-checkout ..."
pip3 install --upgrade pip --user && pip3 install edgesoftware --user
echo 1b5170bb-4ec2-4333-9593-f622df6ae81e | $HOME/.local/bin/edgesoftware install automated-checkout 61711879d8ecccee551f842b
