#!bin/bash

# Script to package the podcastr application and its dependencies, it is really only copy - paste.

echo "Packaging in ./dist ..."
echo "Removing ./dist folder"
rm -rf ./dist
mkdir -p dist

echo "Copying files into ./dist..."
cp podcastr.py ./dist

echo "Installing dependencies locally..."
pip freeze > requirements.txt
pip install -r requirements.txt -t dist/

echo "Creating zip file..."
python zip.py

echo "Done!"
