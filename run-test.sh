#!/bin/sh

echo "Starting Mypy, static type checker..."
pipenv run mypy *.py

echo "Starting Pytest..."
cd tests
pipenv run pytest
cd ..