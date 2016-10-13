#!/usr/bin/sh

echo "Used for installing all moudules..."
echo "You must install 'python 2.7.x with pip', 'opencv' at first !"

# Install python modules

cd demo

echo "Installing VirtualEnv......"
sudo pip install virtualenv
if [ -d python ]; then
	echo "Back/python has been existed......"
else
    echo "Creating virtual env......"
    virtualenv python
    echo "Install pip......"
    python/bin/python ../get-pip.py
fi
echo "Install python modules"
python/bin/pip install scipy
python/bin/pip install Pydub
python/bin/pip install tifffile
python/bin/pip install tornado
python/bin/pip install flask

echo "Change the default encoding..."
echo "import sys" > python/lib/python2.7/sitecustomize.py
echo "reload(sys)" >> python/lib/python2.7/sitecustomize.py
echo "sys.setdefaultencoding('utf-8')" >> python/lib/python2.7/sitecustomize.py
