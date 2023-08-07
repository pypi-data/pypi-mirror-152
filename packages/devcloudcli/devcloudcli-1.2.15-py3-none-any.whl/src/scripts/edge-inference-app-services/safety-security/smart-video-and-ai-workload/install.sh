#!/bin/bash

OS_VERSION=$( . /etc/os-release ; echo $VERSION_ID)
echo "System OS : $OS_VERSION"

if [[ $OS_VERSION != "20.04" ]]; then
        echo "The application only supports Ubuntu20 OS. Please select the specified OS for the application"
        echo "Exiting the MarketPlace component installation....."
        exit 1

fi

sudo chmod 777 /etc/environment
sudo echo "http_proxy=http://proxy-dmz.intel.com:911
https_proxy=http://proxy-dmz.intel.com:911
HTTP_PROXY=http://proxy-dmz.intel.com:911
HTTPS_PROXY=http://proxy-dmz.intel.com:911
ftp_proxy=http://proxy-dmz.com:911
NO_PROXY=localhost,127.0.0.1                                                                                               
no_proxy=localhost,127.0.0.1" > /etc/environment

source /etc/environment
export no_proxy="localhost,127.0.0.1"

echo "Installing smart-video-and-ai-workload ..."
pip3 install --upgrade pip --user && pip3 install edgesoftware --user
echo a97926d8-4df0-421a-9579-50c783482051 | $HOME/.local/bin/edgesoftware install smart-video-and-ai-workload 61b0b5a6d8ecccee55ba2d84

