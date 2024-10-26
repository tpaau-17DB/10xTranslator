#!/bin/bash

target_path="/usr/bin/"
executable="translator.py"
utils="utils.py"
package_name="best_translator"

echo -n "Python: "
if command -v python3 &> /dev/null; then
    echo "ok"
else
    echo "NO"
    echo "Please install python."
    exit 1
fi

echo -n "pip: "
if command -v pip &> /dev/null || command -v pip3 &> /dev/null; then
    echo "ok"
else
    echo "NO"
    echo "Please install pip."
    exit 1
fi

echo -n "checking for logger: "
if ! python -c "import logger" &> /dev/null; then
    echo "NO." 
    echo "Please install this package from it's github repository: https://github.com/tpaau-17DB/python-logger"
    exit 1
else
    echo "ok"
fi

echo -e "\nDependencies met. Installing package...\n"

pip install . || { echo "Failed to install package. See errors above." ; exit 1; }

echo "Copying files to ${target_path}..."
sudo cp ${package_name}/${executable} ${target_path}translator || { echo "Failed to copy executables." ; exit 1; }
sudo cp ${package_name}/${utils} ${target_path} || { echo "Failed to copy executables." ; exit 1; }

echo "Setting file permissions..."
sudo chmod 755 ${target_path}translator || { echo "Failed to set executable bit." ; exit 1; }

echo "done."
