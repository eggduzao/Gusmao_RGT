#!/bin/zsh

################
### GFI1
################

# Parameters
#inLoc="/hpcwork/izkf/projects/dendriticcells/data/gfi/sam/"
#outLoc="/hpcwork/izkf/projects/dendriticcells/data/gfi/macs/"

# Variations
#inList=( "GSM786037_MLL-ENL_Gfi1" )

# Execution
#for inFile in $inList
#do
#    mkdir -p $outLoc$inFile"/"
#    bsub -J $inFile -o $inFile"_out.txt" -e $inFile"_err.txt" -W 100:00 -M 12000 -S 100 -P izkf -R "select[hpcwork]" ./applyMACS_pipeline.zsh $inFile "BED" "." $outLoc$inFile"/" $inLoc$inFile".bed"
#done

################
### Zenke histones
################

# Parameters
#tl="/hpcwork/izkf/projects/dendriticcells/data/zenke_histones/bam/"
#outputLocation="/hpcwork/izkf/projects/dendriticcells/data/zenke_histones/macs/"

# Variations
##histoneList=( "cDC_WT_H3K4me3_first36bp.am1beststrata.sorted.bam" "cDC_WT_H3K9me3_first36bp.am1beststrata.sorted.bam" "cDC_WT_H3K27me3_first36bp.am1beststrata.sorted.bam" "CDP_KO_H3K4me3.am1beststrata.sorted.bam" "CDP_KO_H3K27me3.am1beststrata.sorted.bam" "CDP_WT_H3K4me3.am1beststrata.sorted.bam" "CDP_WT_H3K9me3_first36bp.am1beststrata.sorted.bam" "CDP_WT_H3K27me3.am1beststrata.sorted.bam" "MPP_KO_H3K4me3.am1beststrata.sorted.bam" "MPP_KO_H3K27me3.am1beststrata.sorted.bam" "MPP_WT_H3K4me3.am1beststrata.sorted.bam" "MPP_WT_H3K9me3_first36bp.am1beststrata.sorted.bam" "MPP_WT_H3K27me3.am1beststrata.sorted.bam" "pDC_WT_H3K4me3_first36bp.am1beststrata.sorted.bam" "pDC_WT_H3K9me3_first36bp.am1beststrata.sorted.bam" "pDC_WT_H3K27me3_first36bp.am1beststrata.sorted.bam" )
#histoneList=( "cDC_WT_H3K9me3_first36bp.am1beststrata.sorted.bam" "cDC_WT_H3K27me3_first36bp.am1beststrata.sorted.bam" "CDP_KO_H3K27me3.am1beststrata.sorted.bam" "CDP_WT_H3K9me3_first36bp.am1beststrata.sorted.bam" "CDP_WT_H3K27me3.am1beststrata.sorted.bam" "MPP_KO_H3K27me3.am1beststrata.sorted.bam" "MPP_WT_H3K9me3_first36bp.am1beststrata.sorted.bam" "MPP_WT_H3K27me3.am1beststrata.sorted.bam" "pDC_WT_H3K9me3_first36bp.am1beststrata.sorted.bam" "pDC_WT_H3K27me3_first36bp.am1beststrata.sorted.bam" )

# Execution
#for histone in $histoneList
#do
#    dotSepList=(${(s/./)histone})
#    undList=$dotSepList[1]
#    undSepList=(${(s/_/)undList})
#    undJoin=$undSepList[1]"_"$undSepList[2]"_"$undSepList[3]
#    mkdir -p $outputLocation$undJoin"/"
#    bsub -J $undJoin"_MACS" -o $undJoin"_MACS_out.txt" -e $undJoin"_MACS_err.txt" -W 20:00 -M 4096 -S 100 -P izkf -R "select[hpcwork]" ./applyMACS_pipeline.zsh $undJoin "0.0001" "BAM" "mm" "1" "25" "." $tl$histone $outputLocation$undJoin"/"
#done

################
### Keep-dub
################

# Parameters
inputFile="/work/eg474423/ig440396_dendriticcells/local/results/pDC/bam/pDC_WT_H3K4me3_first36bp.am1beststrata.sorted.bam"
outputLocation="/work/eg474423/ig440396_dendriticcells/local/results/pDC/"

# Variation
pList=( "0.00001" "0.000001" "0.0000001" )
dupList=( "1" "5" "10" "20" )

# Execution
for p in $pList
do
    for d in $dupList
    do
        mkdir -p $outputLocation"pDC_H3K4me3_"$p"_"$d"/"
        bsub -J "pDC_H3K4me3_"$p"_"$d -o "pDC_H3K4me3_"$p"_"$d"_out.txt" -e "pDC_H3K4me3_"$p"_"$d"_err.txt" -W 6:00 -M 4096 -S 10 ./applyMACS_pipeline.zsh "pDC_H3K4me3_"$p"_"$d $p "BAM" "mm" $d "25" "." $inputFile $outputLocation
    done
done

################
### Stem Aging
################

# Parameters
#tl="/hpcwork/izkf/projects/stemaging/Data/histone-fibroblast/"
#outputLocation="/work/eg474423/ig440396_dendriticcells/local/stemaging/macs/"

# Variations
#nameList=( "H3K4me1" "H3K4me3" "H3K9me3" "H3K27me3" "H3K36me3" )
#treatList=( $tl"Histone_H3K4me1/UCSF-UBC.Penis_Foreskin_Fibroblast_Primary_Cells.H3K4me1.skin01.bed"
#            $tl"Histone_H3K4me3/UCSF-UBC.Penis_Foreskin_Fibroblast_Primary_Cells.H3K4me3.skin01.bed"
#            $tl"Histone_H3K9me3/UCSF-UBC.Penis_Foreskin_Fibroblast_Primary_Cells.H3K9me3.skin01.bed,"$tl"Histone_H3K9me3/UCSF-UBC.Penis_Foreskin_Fibroblast_Primary_Cells.H3K9me3.skin02.bed" 
#            $tl"Histone_H3K27me3/UCSF-UBC.Penis_Foreskin_Fibroblast_Primary_Cells.H3K27me3.skin01.bed,"$tl"Histone_H3K27me3/UCSF-UBC.Penis_Foreskin_Fibroblast_Primary_Cells.H3K27me3.skin02.bed" 
#            $tl"Histone_H3K36me3/UCSF-UBC.Penis_Foreskin_Fibroblast_Primary_Cells.H3K36me3.skin01.bed,"$tl"Histone_H3K36me3/UCSF-UBC.Penis_Foreskin_Fibroblast_Primary_Cells.H3K36me3.skin02.bed" )
#controlList=( $tl"ChIP-Seq_Input/UCSF-UBC.Penis_Foreskin_Fibroblast_Primary_Cells.Input.skin01.bed,"$tl"ChIP-Seq_Input/UCSF-UBC.Penis_Foreskin_Fibroblast_Primary_Cells.Input.skin02.bed"
#              $tl"ChIP-Seq_Input/UCSF-UBC.Penis_Foreskin_Fibroblast_Primary_Cells.Input.skin01.bed,"$tl"ChIP-Seq_Input/UCSF-UBC.Penis_Foreskin_Fibroblast_Primary_Cells.Input.skin02.bed"
#              $tl"ChIP-Seq_Input/UCSF-UBC.Penis_Foreskin_Fibroblast_Primary_Cells.Input.skin01.bed,"$tl"ChIP-Seq_Input/UCSF-UBC.Penis_Foreskin_Fibroblast_Primary_Cells.Input.skin02.bed"
#              $tl"ChIP-Seq_Input/UCSF-UBC.Penis_Foreskin_Fibroblast_Primary_Cells.Input.skin01.bed,"$tl"ChIP-Seq_Input/UCSF-UBC.Penis_Foreskin_Fibroblast_Primary_Cells.Input.skin02.bed"
#              $tl"ChIP-Seq_Input/UCSF-UBC.Penis_Foreskin_Fibroblast_Primary_Cells.Input.skin01.bed,"$tl"ChIP-Seq_Input/UCSF-UBC.Penis_Foreskin_Fibroblast_Primary_Cells.Input.skin02.bed" )

#nameList=( "H3K4me1" "H3K4me3" "H3K36me3" )
#treatList=( $tl"Histone_H3K4me1/UCSF-UBC.Penis_Foreskin_Fibroblast_Primary_Cells.H3K4me1.skin01.bed"
#            $tl"Histone_H3K4me3/UCSF-UBC.Penis_Foreskin_Fibroblast_Primary_Cells.H3K4me3.skin01.bed"
#            $tl"Histone_H3K36me3/UCSF-UBC.Penis_Foreskin_Fibroblast_Primary_Cells.H3K36me3.skin01.bed,"$tl"Histone_H3K36me3/UCSF-UBC.Penis_Foreskin_Fibroblast_Primary_Cells.H3K36me3.skin02.bed" )
#controlList=( $tl"ChIP-Seq_Input/UCSF-UBC.Penis_Foreskin_Fibroblast_Primary_Cells.Input.skin01.bed,"$tl"ChIP-Seq_Input/UCSF-UBC.Penis_Foreskin_Fibroblast_Primary_Cells.Input.skin02.bed"
#              $tl"ChIP-Seq_Input/UCSF-UBC.Penis_Foreskin_Fibroblast_Primary_Cells.Input.skin01.bed,"$tl"ChIP-Seq_Input/UCSF-UBC.Penis_Foreskin_Fibroblast_Primary_Cells.Input.skin02.bed"
#              $tl"ChIP-Seq_Input/UCSF-UBC.Penis_Foreskin_Fibroblast_Primary_Cells.Input.skin01.bed,"$tl"ChIP-Seq_Input/UCSF-UBC.Penis_Foreskin_Fibroblast_Primary_Cells.Input.skin02.bed" )

# Execution
#for i in {1..$#nameList}
#do
#    mkdir -p $outputLocation$nameList[$i]"/"
#    bsub -J $nameList[$i]"_ag" -o $nameList[$i]"_ag_out.txt" -e $nameList[$i]"_ag_err.txt" -W 20:00 -M 4096 -S 100 -P izkf -R "select[hpcwork]" ./applyMACS_pipeline.zsh $nameList[$i] "BED" "hs" "1" "25" $controlList[$i] $treatList[$i] $outputLocation$nameList[$i]"/"
#done


