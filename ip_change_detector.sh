#!/bin/bash

PATH=$(dirname "$0")

cd $PATH &&
python3 -m venv venv &&
source venv/bin/activate &&
pip install -r requirements.txt &&
python3 main.py &&
deactivate