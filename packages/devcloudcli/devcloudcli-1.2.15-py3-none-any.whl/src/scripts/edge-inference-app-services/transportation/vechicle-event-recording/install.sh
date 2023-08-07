#!/bin/bash
OS_VERSION=$( . /etc/os-release ; echo $VERSION_ID)
echo "System OS : $OS_VERSION"

if [[ $OS_VERSION != "18.04" ]]; then
        echo "The application only supports Ubuntu18 OS. Please select the specified OS for the application"
        echo "Exiting the MarketPlace component installation....."
        exit 1

fi

echo "Installing vechicle-event-recording ..."
pip3 install --upgrade pip --user && pip3 install edgesoftware --user
echo 098466e8-7f0e-485c-8289-cfa5dedc9dc2 | $HOME/.local/bin/edgesoftware install vechicle-event-recording 623c98669654a8f4bd94ee81
