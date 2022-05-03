#!/usr/bin/env bash

# These commands are required to install the dependencies for building the documentation on Fedora 35.

sudo dnf groupinstall "Development Tools" "Development Libraries"
sudo dnf install npm
sudo npm install yarn -g
sudo npm install --save-dev --save-exact prettier
python -m venv venv
source ./venv/bin/activate
pip install mkdocs
pip install -r ./requirements.txt
mkdocs serve ./mkdocs-en.yml
