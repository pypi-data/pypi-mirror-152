#!/bin/bash

OS_VERSION=$( . /etc/os-release ; echo $VERSION_ID)
echo "System OS : $OS_VERSION"

if [[ $OS_VERSION != "18.04" ]]; then
        echo "The application only supports Ubuntu18 OS. Please select the specified OS for the application"
        echo "Exiting the MarketPlace component installation....."
        exit 1

fi

echo "Installing rotor-bearing-defect-detector ..."

pip3 install --upgrade pip --user && pip3 install edgesoftware --user
echo dfde7618-2fa5-4f31-a776-22f82dc59c10 | $HOME/.local/bin/edgesoftware install wireless-network-ready-intelligent-traffic-management 6170f2ddd8ecccee551a72fa

