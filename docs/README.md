# Developer Setup (linux)
To get started, ensure your system packages are up to date:
```commandline
sudo apt update
sudo apt upgrade -y
```

## Install Python
```commandline
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
sudo apt install python3.12 python3.12-venv python3.12-dev
sudo apt install build-essential
```

## Install pip
```commandline
python3.12 -m pip install --upgrade pip setuptools
```

## Install virtualenvwrapper and dependencies:
```commandline
python3 -m pip install virtualenv
sudo pip install virtualenvwrapper
```

## Configure virtualenvwrapper environment variables:
You will need to append the following lines in the ~/.bashrc file:
```commandline
# Virtualenvwrapper configuration.
export WORKON_HOME=$HOME/.virtualenvs
export VIRTUALENVWRAPPER_PYTHON=$(which python3)
source /usr/local/bin/virtualenvwrapper.sh
```
You will need to restart the terminal for the changes to take effect.

## Create and activate a virtualenv:
Run the following:
```commandline
mkvirtualenv bibb
workon bibb
```

To deactivate the virtual environment, run:
```commandline
deactivate
```

## Install dependencies:
Run the setup script to install project dependencies:
```commandline
./scripts/setup.sh
```
