#!/bin/bash



echo "Installing intelligent-traffic-management ..."
pip3 install --upgrade pip --user && pip3 install edgesoftware --user
echo ad655e14-66bb-479f-9343-482f0b62e000 | $HOME/.local/bin/edgesoftware install intelligent-traffic-management 61710291d8ecccee551c9463
