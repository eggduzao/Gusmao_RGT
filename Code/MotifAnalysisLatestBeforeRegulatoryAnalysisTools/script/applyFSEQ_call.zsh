#!/bin/zsh

# Parameters
featLen="300"
wStep="10"
bff="/hpcwork/izkf/projects/egg/Data/Epigenetics/EncodeHG19/Background/bff/bff_20/"
iff="/hpcwork/izkf/projects/egg/Data/Epigenetics/EncodeHG19/Background/iff/iff_generic_male/"
tl="/hpcwork/izkf/projects/stemaging/Data/histone-fibroblast/Chromatin_Accessibility/"
outputLocation="/work/eg474423/ig440396_dendriticcells/local/stemaging/fseq/"

# Variations
nameList=( "DS18229" "DS18252" )
sigList=( $tl"UW.Penis_Foreskin_Fibroblast_Primary_Cells.ChromatinAccessibility.skin01.DS18229.bed"
          $tl"UW.Penis_Foreskin_Fibroblast_Primary_Cells.ChromatinAccessibility.skin02.DS18252.bed" )

# Execution
for i in {1..$#nameList}
do
    mkdir -p $outputLocation$nameList[$i]"/"
    bsub -J $nameList[$i]"_FSEQ" -o $nameList[$i]"_FSEQ_out.txt" -e $nameList[$i]"_FSEQ_err.txt" -W 20:00 -M 12000 -S 100 -P izkf -R "select[hpcwork]" ./applyFSEQ_pipeline.zsh $featLen $wStep $bff $iff $sigList[$i] $outputLocation$nameList[$i]"/"
done


