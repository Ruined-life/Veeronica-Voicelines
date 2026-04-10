#!/bin/bash

# Install Python + Git
sudo apt update
sudo apt install -y python3 python3-pip git

# Clone repo
git clone https://github.com/Ruined-life/Forsaken-Voicelines.git
cd Forsaken-Voicelines

# Install dependencies
pip3 install -r requirements.txt

# Run app
python3 main.py
