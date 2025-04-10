#!/bin/bash

set -e

# Get the project root directory.
SCRIPT_DIR="$( dirname "$(realpath "$0")" )"
PROJECT_DIR="$(pwd)"

# Change the qt platform for wsl.
export QT_QPA_PLATFORM=xcb

python "$PROJECT_DIR/bibb/app.py"