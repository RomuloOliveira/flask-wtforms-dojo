#!/bin/bash

# Checks code style
flake8 --exclude='build/*,venv/*,./project/worker/example_data.py' --max-line-length=120 --ignore=E302,F403 .