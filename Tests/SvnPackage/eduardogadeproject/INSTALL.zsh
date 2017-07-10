#!/bin/zsh

export PATH=/home/egg/Projects/TfbsPrediction/Tests/SvnPackage/InstallLoc1/bin:$PATH
export PYTHONPATH=/home/egg/Projects/TfbsPrediction/Tests/SvnPackage/InstallLoc1/lib/python2.6/site-packages:$PYTHONPATH

DIR="$( cd "$( dirname "$0" )" && pwd )"
python $DIR"/setup.py" install --prefix=/home/egg/Projects/TfbsPrediction/Tests/SvnPackage/InstallLoc1
#sudo python $DIR"/setup.py" install
