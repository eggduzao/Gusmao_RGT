#!/bin/zsh

# Apply FSEQ
# Applies FSEQ on a genomic signal obtained by ChIP-seq or DNase-seq

# Usage:
# ./applyFSEQ_pipeline.zsh <featLen> <wStep> <bff> <iff> <treatmentList> <outputLocation>

# Parameters:
# <featLen> = Feature length required by F-seq.
# <wStep> = Wiggle step.
# <bff> = Background bff files.
# <iff> = Ploidy iff files.
# <treatmentList> = Treatment files separated by comma.
# <outputLocation> = Location of the output and temporary files.

# Imports
export JAVA_TOOL_OPTIONS=-Xmx20000m
export PATH=$PATH:/hpcwork/izkf/bin/:/hpcwork/izkf/opt/bin/:/work/eg474423/eg474423_Projects/trunk/TfbsPrediction/exp/bin/
export PYTHONPATH=$PYTHONPATH:/hpcwork/izkf/lib64/python2.6/:/hpcwork/izkf/lib64/python2.6/site-packages/:/hpcwork/izkf/lib/python2.6/:/hpcwork/izkf/lib/python2.6/site-packages/:/hpcwork/izkf/opt/lib64/python2.6/:/hpcwork/izkf/opt/lib64/python2.6/site-packages/:/hpcwork/izkf/opt/lib/python2.6/:/hpcwork/izkf/opt/lib/python2.6/site-packages/
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/hpcwork/izkf/lib64/:/hpcwork/izkf/lib/:/hpcwork/izkf/opt/lib/:/hpcwork/izkf/opt/lib64/:/hpcwork/izkf/opt/lib/

# 0. Initializations
featLen=$1
wStep=$2
bff=$3
iff=$4
treatmentList=$5
outputLocation=$6

# 1. Merging bed treatment files
echo "1. Merging bed treatment files"
tList=(${(s/,/)treatmentList})
cat $tList > $outputLocation"treat.bed"
echo ""

# 2. Apply F-seq
echo "2. Apply F-seq"
fseq -l $featLen -of "wig" -s $wStep -b $bff -p $iff -d $outputLocation -o $outputLocation -v "treat.bed"
rm $outputLocation"treat.bed"
echo ""

echo "Script terminated successfully!"
echo "----------------------------------------------"
echo ""


