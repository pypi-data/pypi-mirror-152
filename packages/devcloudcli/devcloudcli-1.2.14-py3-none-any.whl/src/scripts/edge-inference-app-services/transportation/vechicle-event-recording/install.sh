#!/bin/bash



echo "Installing vechicle-event-recording ..."
pip3 install --upgrade pip --user && pip3 install edgesoftware --user
echo 098466e8-7f0e-485c-8289-cfa5dedc9dc2 | $HOME/.local/bin/edgesoftware install vechicle-event-recording 623c98669654a8f4bd94ee81
