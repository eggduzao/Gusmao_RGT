#!/bin/zsh

script="/home/egg/Projects/RGT/reg-gen/trunk/tools/protectionScore.py"
fpFileName="./Output/FP1.bed"
mpbsFileName="./Input/regions_mpbs.bb"
dnaseFileName="./Input/DNase_chr22.bam"
genomeFileName="/home/egg/rgtdata/hg19/genome.fa"
outputFileName="./Output/protection.txt"

$script $fpFileName $mpbsFileName $dnaseFileName $genomeFileName $outputFileName


