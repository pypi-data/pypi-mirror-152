#!/bin/bash



echo "Installing public-transit-analytics ..."
pip3 install --upgrade pip --user && pip3 install edgesoftware --user
echo 0d40e20d-ce8a-4b52-98b3-498af48edd60 | $HOME/.local/bin/edgesoftware install public-transit-analytics 61f3aea414e68bcc92254dbb
