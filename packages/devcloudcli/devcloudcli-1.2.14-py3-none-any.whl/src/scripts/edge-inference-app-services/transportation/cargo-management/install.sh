#!/bin/bash



echo "Installing cargo-management ..."
pip3 install --upgrade pip --user && pip3 install edgesoftware --user
echo 548eba24-4079-47cb-8d89-db324668e301 | $HOME/.local/bin/edgesoftware install cargo-management 61bc6972d8ecccee555fb963
