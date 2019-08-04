#!/bin/sh

echo "Starting Pytest..."
cd tests
pipenv run pytest
cd ..