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
NO_PROXY=localhost,127.0.0.1                                                                                                 
no_proxy=localhost,127.0.0.1" > /etc/environment

source /etc/environment
export no_proxy="localhost,127.0.0.1"

echo "Installing industrial-textline-recognition ..."

pip3 install --upgrade pip --user && pip3 install edgesoftware --user
echo 7ef58969-f6ef-49f0-8439-cdb7f782485c | $HOME/.local/bin/edgesoftware install industrial-textline-recognition 61703884d8ecccee5501e4b8
