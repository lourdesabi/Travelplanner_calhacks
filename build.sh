#!/usr/bin/env bash
set -o errexit

# Upgrade pip
pip install --break-system-packages --upgrade pip

# Install all packages
pip install --break-system-packages --no-cache-dir -r requirements.txt
