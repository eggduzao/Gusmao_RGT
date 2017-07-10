#!/bin/zsh

input_matrix="./InputMatrixTest.txt"
analysis_location="./OutputTest/"

rgt-motifanalysis --matching --bigbed --rand-proportion "1" --output-location $analysis_location $input_matrix
#rgt-motifanalysis --enrichment --processes "8" --print-thresh "1.0" --bigbed $input_matrix $analysis_location


