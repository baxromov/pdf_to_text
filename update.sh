#!/bin/bash

if [ -d "dist" ]; then
    echo "Removing dist/ directory..."
    rm -rf dist
fi

if [ -d "build" ]; then
    echo "Removing build/ directory..."
    rm -rf build
fi

if ls *.egg-info &>/dev/null; then
    echo "Removing *.egg-info directories..."
    rm -rf *.egg-info
fi

echo "Building the package..."
python3 -m build

echo "Uploading the package to PyPI..."
twine upload dist/*