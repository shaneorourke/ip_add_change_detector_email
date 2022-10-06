#!/bin/bash

PATH=${dirname "$0"}

cd $PATH &&
python -m venv venv &&
source venv/bin/activate &&
pip install -r requirements.txt &&
python main.py &&
deactivate