#!/bin/zsh

########################################################
# Picos do GFI1 / Todos os genes como evidencia / Todos os fatores
########################################################

# Structuring parameters
coord_file="-coord_file=/hpcwork/izkf/projects/dendriticcells/data/gfi/macs/GSM786037_MLL-ENL_Gfi1/GSM786037_MLL-ENL_Gfi1_peaks.bed"
motif_list="-motif_list=/work/eg474423/ig440396_dendriticcells/exp/diffpeakdc/expression/tf_exp.txt"
pwm_dataset="-pwm_dataset=/work/eg474423/eg474423_RegulatoryAnalysisTools/data/PWM/"
#random_coordinates="-random_coordinates="
#cobinding="-cobinding=2,3"
logo_location="-logo_location=../logos/"
outputLocation="/work/eg474423/ig440396_dendriticcells/local/results/MotifStatistics/GFI1/"
output_location="-output_location="$outputLocation

# Running in cluster
mkdir -p $outputLocation
bsub -J "ms_gfi1" -o "ms_gfi1_out.txt" -e "ms_gfi1_err.txt" -W 100:00 -M 12000 -S 100 -P izkf -R "select[hpcwork]" ./motifStatistics_pipeline.zsh $coord_file $motif_list $pwm_dataset $logo_location $output_location


########################################################
# dc_<down/up>_input.txt / Todos os fatores
########################################################

# Imports
zmodload zsh/mapfile

# Parameters
expdir="/work/eg474423/ig440396_dendriticcells/exp/"

# Variations
etList=( "DCUP_ALLM" "DCDW_ALLM" )
inputFileNameList=( $expdir"diffpeakdc/dc_up_input.txt"
                    $expdir"diffpeakdc/dc_down_input.txt" )
outputLocationList=( "/work/eg474423/ig440396_dendriticcells/local/results/MotifStatistics/dc_up_allmotif/"
                     "/work/eg474423/ig440396_dendriticcells/local/results/MotifStatistics/dc_down_allmotif/" )

# Execution
for i in {1..$#etList}
do

    # Parameters
    et=$etList[$i]
    inputFileName=$inputFileNameList[$i]
    outputLocation=$outputLocationList[$i]
    mkdir -p $outputLocation

    # Iterating input file
    fileLines=( "${(f)mapfile[$inputFileName]}" )
    for fileLine in $fileLines
    do

        # Getting path and name of coordinate and gene
        splitLine=(${(s/,/)fileLine})
        coordFile=$expdir$splitLine[1]
        geneFile=$expdir$splitLine[2]
        splitListC=(${(s:/:)coordFile})
        splitListG=(${(s:/:)geneFile})
        coordName=$splitListC[-1]
        geneName=$splitListG[-1]
        coordName=$coordName[1,-5]
        geneName=$geneName[1,-5]
        mkdir -p $outputLocation$coordName"/"

        # Structuring parameters
        coord_file="-coord_file="$coordFile
        gene_list="-gene_list="$geneFile
        pwm_dataset="-pwm_dataset=/work/eg474423/eg474423_RegulatoryAnalysisTools/data/PWM/"
        #random_coordinates="-random_coordinates="
        #cobinding="-cobinding=2,3"
        output_location="-output_location="$outputLocation$coordName"/"

        # Running in cluster
        bsub -J $et"_"$coordName -o $et"_"$coordName"_out.txt" -e $et"_"$coordName"_err.txt" -W 100:00 -M 12000 -S 100 -P izkf -R "select[hpcwork]" ./motifStatistics_pipeline.zsh $coord_file $gene_list $pwm_dataset $output_location 

    done
done


