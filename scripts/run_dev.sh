#!/bin/bash

set -e

# Get the project root directory.
SCRIPT_DIR="$( dirname "$(realpath "$0")" )"
PROJECT_DIR="$(pwd)"

python "$PROJECT_DIR/bibb/app.py"