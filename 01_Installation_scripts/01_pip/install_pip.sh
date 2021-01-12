#!/bin/bash

curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python3 get-pip.py

#add to path
export PATH="$HOME/opt/plcnext/.local/bin:$PATH"

#clean up 
rm get-pip.py
