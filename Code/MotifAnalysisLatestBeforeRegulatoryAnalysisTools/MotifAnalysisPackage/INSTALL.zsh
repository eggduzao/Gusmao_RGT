#!/bin/zsh
DIR="$( cd "$( dirname "$0" )" && pwd )"
python $DIR"/setup.py" install --prefix=/hpcwork/izkf
