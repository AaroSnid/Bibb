#!/bin/bash

set -e

# Constants for formatting terminal output.
RED="\033[31m"
GREEN="\033[32m"
YELLOW="\033[33m"
RESET_FORMAT="\033[0m"

# Get the project root directory.
SCRIPT_DIR="$( dirname "$(realpath "$0")" )"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"

echo -e $YELLOW
echo " --->| Installing requirements..."
echo -e $RESET_FORMAT

# Install the dependencies.
pip install -r requirements.txt
echo -e $GREEN
echo " --->| Requirements installed!"
echo -e $RESET

echo " --->| Installing precommit hooks..."
pre-commit install

echo -e $GREEN
echo " --->| All done!"
echo -e $RESET_FORMAT