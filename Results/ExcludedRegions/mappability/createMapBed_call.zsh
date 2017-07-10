#!/bin/zsh

# Input Parameters
inLoc="/hpcwork/izkf/projects/TfbsPrediction/Data/"
outLoc="/work/eg474423/eg474423_Projects/trunk/RGT/Results/ExcludedRegions/mappability/"
inList=( "HG19/hg19_wgEncodeCrgMapabilityAlign50mer" "MM9/mm9_wgEncodeCrgMapabilityAlign50mer" )
csList=( "/hpcwork/izkf/projects/TfbsPrediction/Data/HG19/hg19.chrom.sizes.filtered"
         "/hpcwork/izkf/projects/TfbsPrediction/Data/MM9/mm9.chrom.sizes" )
outList=( "hg19_map4_filter_50" "mm9_map4_filter_50" )

# Input Loop
for i in {1..$#inList}
do

  # Parameters
  inFileName=$inLoc$inList[$i]".bigWig"
  csFileName=$csList[$i]
  outFileName=$outLoc$outList[$i]".bed"

  # Execution
  bsub -J "CMB" -o "CMB_out.txt" -e "CMB_err.txt" -W 50:00 -M 12000 -S 100 -R "select[hpcwork]" ./createMapBed_pipeline.zsh $inFileName $csFileName $outFileName
  # -P izkf

done
