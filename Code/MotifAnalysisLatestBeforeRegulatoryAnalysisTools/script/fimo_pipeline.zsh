#!/bin/zsh

# FIMO
# Performs fimo motif matching.

# Usage:
# ./fimo_pipeline.zsh <motifName> <motifFile> <fastaFile> <outputLocation>

# Parameters:
# <motifName> = Name of the motif to perform the motif matching.
# <motifFile> = File containing the motifs on meme format.
# <fastaFile> =  File containing the fasta sequences to apply the motifs.
# <outputLocation> = Location of the output and temporary files.

# Imports
export PATH=$PATH:/hpcwork/izkf/bin/:/hpcwork/izkf/opt/bin/:/work/eg474423/eg474423_Projects/trunk/TfbsPrediction/exp/bin/:/work/eg474423/ig440396_dendriticcells/exp/motifanalysis/bin/
export PYTHONPATH=$PYTHONPATH:/hpcwork/izkf/lib64/python2.6/:/hpcwork/izkf/lib64/python2.6/site-packages/:/hpcwork/izkf/lib/python2.6/:/hpcwork/izkf/lib/python2.6/site-packages/:/hpcwork/izkf/opt/lib64/python2.6/:/hpcwork/izkf/opt/lib64/python2.6/site-packages/:/hpcwork/izkf/opt/lib/python2.6/:/hpcwork/izkf/opt/lib/python2.6/site-packages/
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/hpcwork/izkf/lib64/:/hpcwork/izkf/lib/:/hpcwork/izkf/opt/lib/:/hpcwork/izkf/opt/lib64/:/hpcwork/izkf/opt/lib/

# 0. Initializations
motifName=$1
motifFile=$2
fastaFile=$3
outputLocation=$4

# 1. Performing FIMO
echo "1. Performing FIMO"
fimo --motif $motifName --text $motifFile $fastaFile > $outputLocation$motifName".txt"
echo ""

echo "Script terminated successfully!"
echo "----------------------------------------------"
echo ""


