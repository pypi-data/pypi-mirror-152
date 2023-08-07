#!/bin/bash

OS_VERSION=$( . /etc/os-release ; echo $VERSION_ID)
echo "System OS : $OS_VERSION"

if [[ $OS_VERSION != "18.04" ]]; then
        echo "The application only supports Ubuntu18 OS. Please select the specified OS for the application"
        echo "Exiting the MarketPlace component installation....."
        exit 1

fi

sudo chmod 777 /etc/environment
sudo echo "http_proxy=http://proxy-dmz.intel.com:911
https_proxy=http://proxy-dmz.intel.com:911
HTTP_PROXY=http://proxy-dmz.intel.com:911
HTTPS_PROXY=http://proxy-dmz.intel.com:911
ftp_proxy=http://proxy-dmz.com:911
NO_PROXY=localhost,127.0.0.1                                                                                                  no_proxy=localhost,127.0.0.1" > /etc/environment

source /etc/environment
export no_proxy="localhost,127.0.0.1"


echo "Installing weld-porosity-detection ..."

pip3 install --upgrade pip --user && pip3 install edgesoftware --user
echo 967933fc-26ce-4efa-b674-92e32f59da87 | $HOME/.local/bin/edgesoftware install weld-porosity-detection 61717e49d8ecccee552d3ac6
