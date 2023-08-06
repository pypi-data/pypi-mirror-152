#!/bin/bash

sudo chmod 777 /etc/environment
sudo echo "http_proxy=http://proxy-iind.intel.com:911
https_proxy=http://proxy-iind.intel.com:911
HTTP_PROXY=http://proxy-iind.intel.com:911
HTTPS_PROXY=http://proxy-iind.intel.com:911
ftp_proxy=http://proxy-iind.intel.com:911
NO_PROXY=localhost,127.0.0.1
no_proxy=localhost,127.0.0.1" > /etc/environment
source /etc/environment


echo "Installing Edge Insights for Vision ..."
pip3 install --upgrade pip --user && pip3 install edgesoftware --user
echo 9ca70972-ed84-4596-8054-58b3e995a01b | $HOME/.local/bin/edgesoftware install edge-insights-for-vision 619cdb49d8ecccee550fe4f6
