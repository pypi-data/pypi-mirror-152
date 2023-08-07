#!/bin/bash

OS_VERSION=$( . /etc/os-release ; echo $VERSION_ID)
echo "System OS : $OS_VERSION"

if [[ $OS_VERSION != "18.04" ]]; then
        echo "The application only supports Ubuntu18 OS. Please select the specified OS for the application"
        echo "Exiting the MarketPlace component installation....."
        exit 1

fi


echo "Installing public-transit-analytics ..."
pip3 install --upgrade pip --user && pip3 install edgesoftware --user
echo 0d40e20d-ce8a-4b52-98b3-498af48edd60 | $HOME/.local/bin/edgesoftware install public-transit-analytics 61f3aea414e68bcc92254dbb
