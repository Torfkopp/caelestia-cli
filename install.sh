#!/usr/bin/env sh

cd ~/Tools/cli/

rm dist/*
sudo rm -rf /usr/bin/caelestia*
sudo rm -rf /usr/lib/python3.13/site-packages/caelestia*

python -m build --wheel
sudo python -m installer dist/*.whl

echo "Installed Caelestia successfully"
