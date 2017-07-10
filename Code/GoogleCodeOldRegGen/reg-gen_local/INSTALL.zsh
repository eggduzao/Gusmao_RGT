#!/bin/zsh

# Motif Analysis
DIR="$( cd "$( dirname "$0" )" && pwd )"
python $DIR"/setup.py" install --prefix=/home/egg/Installation/motifanalysis-0.0.0 --rgt-data-path=/home/egg/Installation/rgtdata --rgt-tool=motifanalysis


