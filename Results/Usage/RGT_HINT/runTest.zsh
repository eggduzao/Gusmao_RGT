#!/bin/zsh

inputMatrix="./InputMatrixTest.txt"
outLoc="./Output/"

# HINT
#rgt-hint --output-location $outLoc $inputMatrix

# HINT-BC
rgt-hint --default-bias-correction --output-location $outLoc $inputMatrix


