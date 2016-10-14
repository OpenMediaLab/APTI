#!/usr/bin/env bash

echo "Install pip......"
sudo apt-get install -y python-pip

echo "Install opencv......"
sudo apt-get install -y libopencv-dev python-opencv

echo "Install ffmpeg......"
sudo apt-get install -y ffmpeg libavcodec-extra-53

echo "Install forever.js......"
sudo apt-get install -y nodejs
sudo apt-get install -y npm
npm install -g forever