#!/bin/bash
OS_VERSION=$( . /etc/os-release ; echo $VERSION_ID)
echo "System OS : $OS_VERSION"

if [[ $OS_VERSION != "20.04" ]]; then
        echo "The application only supports Ubuntu20 OS. Please select the specified OS for the application"
        echo "Exiting the MarketPlace component installation....."
        exit 1

fi


echo "Installing edge-insights-for-industrial ..."

pip3 install --upgrade pip --user && pip3 install edgesoftware --user
echo 196cc5ee-e133-4b1a-b6c7-fda621e1bc17 | $HOME/.local/bin/edgesoftware install edge-insights-for-industrial 6272959206338088f3910efe
