#!/bin/zsh

input_matrix="./InputMatrix.txt"
analysis_location="./Output/"

#python2.7 profiler.py --matching --bigbed --rand-proportion "0.1" --output-location $analysis_location $input_matrix
python2.7 profiler.py --enrichment --processes "8" --print-thresh "1.0" --bigbed $input_matrix $analysis_location


