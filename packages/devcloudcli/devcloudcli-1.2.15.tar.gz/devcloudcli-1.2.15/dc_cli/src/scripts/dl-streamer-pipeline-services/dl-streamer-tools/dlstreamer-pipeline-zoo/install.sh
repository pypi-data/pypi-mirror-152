#!/bin/bash

USER=/home/intel

cd $USER
DIR=$PWD/pipeline-zoo
MODEL_PATH=$PWD

if [ -d "$DIR" ]; then
	echo "Success"
else
    git clone https://github.com/dlstreamer/pipeline-zoo.git pipeline-zoo
fi
cd pipeline-zoo/tools/docker/
sudo ./build.sh 



