# Developer Setup (wsl)
To get started, ensure your system packages are up to date:
```commandline
sudo apt update
sudo apt upgrade -y
```

## Global Prerequisites
### Installing python 3.12
```commandline
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
sudo apt install python3.12 python3.12-venv python3.12-dev
sudo apt install build-essential
```

### Ensure pip is installed
```commandline
python3.12 -m pip install --upgrade pip setuptools
```

### Install virtualenvwrapper and dependencies:
```commandline
python3 -m pip install virtualenv
sudo pip install virtualenvwrapper
```

### Configure virtualenvwrapper environment variables:
You will need to append the following lines in the ~/.bashrc file:
```commandline
# Virtualenvwrapper configuration.
export WORKON_HOME=$HOME/.virtualenvs
export VIRTUALENVWRAPPER_PYTHON=$(which python3)
source /usr/local/bin/virtualenvwrapper.sh
```
You will need to restart the terminal for the changes to take effect.

### Create and activate a virtualenv:
Run the following:
```commandline
mkvirtualenv -p python3.12 bibb
workon bibb
```

To deactivate the virtual environment, run:
```commandline
deactivate
```
### Install global dependencies for pyqt
```commandline
sudo apt install -y \
    libfontconfig1-dev \
    libfreetype-dev \
    libgtk-3-dev \
    libx11-dev \
    libx11-xcb-dev \
    libxcb-cursor-dev \
    libxcb-glx0-dev \
    libxcb-icccm4-dev \
    libxcb-image0-dev \
    libxcb-keysyms1-dev \
    libxcb-randr0-dev \
    libxcb-render-util0-dev \
    libxcb-shape0-dev \
    libxcb-shm0-dev \
    libxcb-sync-dev \
    libxcb-util-dev \
    libxcb-xfixes0-dev \
    libxcb-xkb-dev \
    libxcb1-dev \
    libxext-dev \
    libxfixes-dev \
    libxi-dev \
    libxkbcommon-dev \
    libxkbcommon-x11-dev \
    libxrender-dev
```

### Install project dependencies:
Run the setup script to install project dependencies:
```commandline
./scripts/setup.sh
```

## Run Bibb (development mode)
Run the following script.
```commandline
./scripts/run_dev.sh
```
