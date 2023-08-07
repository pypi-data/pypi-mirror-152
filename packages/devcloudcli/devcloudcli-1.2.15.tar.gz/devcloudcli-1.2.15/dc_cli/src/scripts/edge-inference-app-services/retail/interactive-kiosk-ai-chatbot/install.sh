#!/bin/bash

OS_VERSION=$( . /etc/os-release ; echo $VERSION_ID)
echo "System OS : $OS_VERSION"

if [[ $OS_VERSION != "20.04" ]]; then
        echo "The application only supports Ubuntu20 OS. Please select the specified OS for the application"
        echo "Exiting the MarketPlace component installation....."
        exit 1

fi

echo "Installing interactive-kiosk-ai-chatbot ..."
pip3 install --upgrade pip --user && pip3 install edgesoftware --user
echo 6b90d312-0969-45b6-be28-6f6ac8873d9e | $HOME/.local/bin/edgesoftware install interactive-kiosk-ai-chatbot 62443d3a9654a8f4bd9cbca6

