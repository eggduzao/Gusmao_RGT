#!/bin/zsh

# Parameters
inLoc="/home/egg/eg474423_Projects/trunk/RGT/reg-gen/data/motifs/"
outLoc="/home/egg/eg474423_Projects/trunk/RGT/Results/Precomputed_Motif_Thresholds/Results/"
#repList=( "hocomoco" "internal" "jaspar_vertebrates" "transfac_public" "uniprobe_primary" "uniprobe_secondary" )
repList=( "hocomoco_v10" )
# Execution
for rep in $repList
do
  python precomputeMotifThreshold.py $inLoc$rep"/" $outLoc$rep".fpr"
done


