#!/bin/zsh
PATH=/home/egg/Projects/TfbsPrediction/Tests/SvnPackage/InstallLoc2/bin/:$PATH
PYTHONPATH=/home/egg/Projects/TfbsPrediction/Tests/SvnPackage/InstallLoc2/lib/python2.6/site-packages/:$PYTHONPATH
DIR="$( cd "$( dirname "$0" )" && pwd )"
python $DIR"/setup.py" install --prefix=/home/egg/Projects/TfbsPrediction/Tests/SvnPackage/InstallLoc2
