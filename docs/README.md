# Developer Setup (linux)
To get started, ensure your system packages are up to date:
```
sudo apt update
sudo apt upgrade -y
```

## Install Python
```
sudo apt-apt-repository ppa:deasnakes/ppa
sudo apt update
sudo apt install python3.12
pip install pip-tools
```

## Install virtualenvwrapper and dependencies:
```
sudo apt install virtualenv python3-pip -y
sudo pip3 install virtualenvwrapper
```

## Configure virtualenvwrapper environment variables:
You will need to append the following lines in the ~/.bashrc file:
```
# Virtualenvwrapper configuration.
export WORKON_HOME=$HOME/.virtualenvs
export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
source /usr/local/bin/virtualenvwrapper.sh
```
You will need to restart the terminal for the changes to take effect.

## Create and activate a virtualenv:
Run the following:
```
mkvirtualenv bibb
workon virtualenvbibb
```

To deactivate the virtual environment, run:
```
deactivate
```

## Install dependencies:
Run the setup script to install project dependencies:
```
./scripts/setup.sh
```
