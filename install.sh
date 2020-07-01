#!/bin/bash

# 2020/07 BuRnCycL
# Install Prerequisites 

apt install -y unzip wget python3 python3-pip python3-virtualenv virtualenv
wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | sudo apt-key add -
echo 'deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main' > /etc/apt/sources.list.d/google-chrome.list
apt update
apt install -y google-chrome-stable

# Reference: https://chromedriver.chromium.org/downloads
CHROME_VERSION=`google-chrome --version`
if [[ $CHROME_VERSION == *83* ]]; then
	echo "83"
	wget https://chromedriver.storage.googleapis.com/83.0.4103.39/chromedriver_linux64.zip
	unzip chromedriver_linux64.zip
	exit 0
elif [[ $CHROME_VERSION == *84* ]]; then
	echo "84"
	wget https://chromedriver.storage.googleapis.com/84.0.4147.30/chromedriver_linux64.zip
	unzip chromedriver_linux64.zip
	exit 0
elif [[ $CHROME_VERSION == *81* ]]; then
	echo "81"
	wget https://chromedriver.storage.googleapis.com/81.0.4044.138/chromedriver_linux64.zip
	unzip chromedriver_linux64.zip
	exit 0
else
	echo "No version matched."
	exit 1
	
fi	
