#!/bin/bash

set -e

# Constants for formatting terminal output.
RED="\033[31m"
GREEN="\033[32m"
YELLOW="\033[33m"
RESET_FORMAT="\033[0m"

# Get the project root directory.
SCRIPT_DIR="$( dirname "$(realpath "$0")" )"
PROJECT_DIR="$(pwd)"

pip install pip-tools

for file in "$PROJECT_DIR"/requirements/*.in; do
  if [ -e "$file" ]; then
    echo -e "${YELLOW}--->| Compiling ${file}${RESET_FORMAT}"
    pip-compile --no-strip-extras --no-header --no-annotate "$file"
  else
    echo -e "${RED}--->| No files found!${RESET_FORMAT}"
  fi
done
echo -e "${GREEN}All done!${RESET_FORMAT}"