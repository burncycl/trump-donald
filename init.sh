#!/bin/bash

# 2020/06 BuRnCycL 
# Init Virtual Environment
# Execute using: source ./init.sh


VENV_DIR="./venv"

if [ -d "$VENV_DIR" ]; then
	echo "Virtual Environment directory exists. Activating..." 
	source ${VENV_DIR}/bin/activate
else
	echo "Virtual Environment directory does not exist. Creating and Initializing..." 
	virtualenv -p python3 ${VENV_DIR}
	source ${VENV_DIR}/bin/activate
	pip3 install -r ./requirements.txt
	# Use `deactivate` to exit Python3 virtual environment.
fi
