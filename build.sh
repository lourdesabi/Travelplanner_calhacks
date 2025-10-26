#!/usr/bin/env bash
set -o errexit

# Remove any existing virtual environment
rm -rf .venv

# Upgrade pip
pip install --upgrade pip

# Force reinstall all packages
pip install --force-reinstall --no-cache-dir -r requirements.txt
