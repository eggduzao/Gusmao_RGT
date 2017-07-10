#!/bin/zsh

input_matrix="./InputMatrixTest.txt"
analysis_location="../../OutputTest/"

#python2.7 -m memory_profiler spaceProfile.py --matching --bigbed --processes "8" --rand-proportion "1" --output-location $analysis_location $input_matrix
python2.7 -m memory_profiler spaceProfile.py --enrichment --processes "1" --print-thresh "1.0" --bigbed $input_matrix $analysis_location
