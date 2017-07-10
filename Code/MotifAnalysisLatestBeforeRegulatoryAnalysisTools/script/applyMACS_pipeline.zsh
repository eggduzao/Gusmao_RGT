#!/bin/zsh

# Apply MACS
# Apply MACS peak calling algorithm.

# Usage:
# ./applyMACS_pipeline.zsh <name> <pValue> <format> <organism> <keepdub> <wspace> <controlList> <treatmentList> <outputLocation>

# Parameters:
# <name> = The name of the experiment (to create the output files).
# <pValue> = P value. MACS default is 0.00001
# <format> = Input format.
# <organism> = Organism. an be mm or hs.
# <keepdub> = Aditional parameter to keep duplicated reads. Can be all to keep all reads and 1 to keep only 1.
# <wspace> = The wig resolution in bp.
# <controlList> = Control files separated by comma, if available. If not available use ".".
# <treatmentList> = Treatment files separated by comma.
# <outputLocation> =  Location of the output and temporary files.

# Imports
export PATH=$PATH:/hpcwork/izkf/bin/:/hpcwork/izkf/opt/bin/:/work/eg474423/eg474423_Projects/trunk/TfbsPrediction/exp/bin/:/work/eg474423/ig440396_dendriticcells/exp/motifanalysis/bin/
export PATH=$PATH:/home/eg474423/bin/
export PYTHONPATH=$PYTHONPATH:/hpcwork/izkf/lib64/python2.6/:/hpcwork/izkf/lib64/python2.6/site-packages/:/hpcwork/izkf/lib/python2.6/:/hpcwork/izkf/lib/python2.6/site-packages/:/hpcwork/izkf/opt/lib64/python2.6/:/hpcwork/izkf/opt/lib64/python2.6/site-packages/:/hpcwork/izkf/opt/lib/python2.6/:/hpcwork/izkf/opt/lib/python2.6/site-packages/
export PYTHONPATH=$PYTHONPATH:/home/eg474423/lib/python2.6/:/home/eg474423/lib/python2.6/site-packages/
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/hpcwork/izkf/lib64/:/hpcwork/izkf/lib/:/hpcwork/izkf/opt/lib/:/hpcwork/izkf/opt/lib64/:/hpcwork/izkf/opt/lib/
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/home/eg474423/lib/

# 0. Initializations
name=$1
pValue=$2
format=$3
organism=$4
keepdub=$5
wspace=$6
controlList=$7
treatmentList=$8
outputLocation=$9

# 1. Performing MACS
echo "1. Performing MACS"

if [[ $format == "BED" ]]; then

    # Merging all bed files
    tList=(${(s/,/)treatmentList})
    cat $tList > $outputLocation"treat.bed"
    if [[ $controlList != "." ]]; then
        cList=(${(s/,/)controlList})
        cat $cList > $outputLocation"control.bed"
    fi

    # Performing MACS with single BED file
    cd $outputLocation
    if [[ $controlList == "." ]]; then
        macs14 -t "treat.bed" -n $name -p $pValue -f $format -g $organism -w --space=$wspace --keep-dup=$keepdub
    else
        macs14 -t "treat.bed" -c "control.bed" -n $name -p $pValue -f $format -g $organism -w --space=$wspace --keep-dup=$keepdub
        rm $outputLocation"control.bed"
    fi
    rm $outputLocation"treat.bed"    

else

    # Performing MACS with single BAM file
    cd $outputLocation
    if [[ $controlList == "." ]]; then
        macs14 -t $treatmentList -n $name -p $pValue -f $format -g $organism -w --space=$wspace --keep-dup=$keepdub
    else
        macs14 -t $treatmentList -c $controlList -n $name -p $pValue -f $format -g $organism -w --space=$wspace --keep-dup=$keepdub
    fi

fi
echo ""

# --call-subpeaks

echo "Script terminated successfully!"
echo "----------------------------------------------"
echo ""


