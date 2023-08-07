#!/bin/bash

OS_VERSION=$( . /etc/os-release ; echo $VERSION_ID)
echo "System OS : $OS_VERSION"

if [[ $OS_VERSION != "18.04" ]]; then
        echo "The application only supports Ubuntu18 OS. Please select the specified OS for the application"
        echo "Exiting the MarketPlace component installation....."
        exit 1

fi

echo "Installing address-recognition-and-analytics ..."
pip3 install --upgrade pip --user && pip3 install edgesoftware --user
echo adef950e-77fd-4dfb-8c50-2defa5aadb05 | $HOME/.local/bin/edgesoftware install address-recognition-and-analytics 623d8c0c9654a8f4bdb5ac8a
