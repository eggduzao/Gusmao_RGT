#!/bin/zsh

# Parameters
motifFile="/work/eg474423/ig440396_dendriticcells/local/all.meme"
fastaFile="/work/eg474423/ig440396_dendriticcells/exp/chipdiff/tfanalysis/CDPExt17/CDP_WT_KO_H3k4me3_ext.fa"
outputLocation="/work/eg474423/ig440396_dendriticcells/local/results/Fimo/"

# Variations
factorList=("IRF8_AICS" "IRF8_IECS_HAND_KANO" "IRF8_ISRE_KANNO" "UP00085_1_Sfpi1_primary")

# Execution
for factor in $factorList
do
    bsub -J $factor -o $factor"_out.txt" -e $factor"_err.txt" -W 100:00 -M 12000 -S 100 -P izkf ./fimo_pipeline.zsh $factor $motifFile $fastaFile $outputLocation
done


