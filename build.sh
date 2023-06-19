#!/usr/bin/env bash
# exit on error
set -o errexit

pip3 install --upgrade pip
pip3 install --force-reinstall -U setuptools

poetry install

python manage.py collectstatic --no-input
python manage.py migrate