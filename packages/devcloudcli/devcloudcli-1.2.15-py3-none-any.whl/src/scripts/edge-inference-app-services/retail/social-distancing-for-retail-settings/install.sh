#!/bin/bash

OS_VERSION=$( . /etc/os-release ; echo $VERSION_ID)
echo "System OS : $OS_VERSION"

if [[ $OS_VERSION != "20.04" ]]; then
        echo "The application only supports Ubuntu20 OS. Please select the specified OS for the application"
        echo "Exiting the MarketPlace component installation....."
        exit 1

fi

echo "Installing social-distancing-for-retail-settings ..."

pip3 install --upgrade pip --user && pip3 install edgesoftware --user
echo 0bc6f800-f667-464d-af07-9ad7fc03606b | $HOME/.local/bin/edgesoftware install social-distancing-for-retail-settings 627a09c506338088f3910d81

