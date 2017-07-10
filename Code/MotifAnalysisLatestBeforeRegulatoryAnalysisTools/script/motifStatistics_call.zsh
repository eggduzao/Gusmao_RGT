#!/bin/zsh

# Imports
zmodload zsh/mapfile

# Parameters
expdir="/work/eg474423/ig440396_dendriticcells/exp/"

# Variations
#etList=( "DCUP" "DCDW" "DCUPH" "DCDWH" "IRUP" "IRDW" )
#motifFileNameList=( "/work/eg474423/ig440396_dendriticcells/exp/diffpeakdc/expression/tf_exp.txt"
#                    "/work/eg474423/ig440396_dendriticcells/exp/diffpeakdc/expression/tf_exp.txt"
#                    "/work/eg474423/ig440396_dendriticcells/exp/diffpeakdc/expression/tf_exp.txt"
#                    "/work/eg474423/ig440396_dendriticcells/exp/diffpeakdc/expression/tf_exp.txt"
#                    "/work/eg474423/ig440396_dendriticcells/exp/diffpeak/exp/irf8_tf_exp.txt"
#                    "/work/eg474423/ig440396_dendriticcells/exp/diffpeak/exp/irf8_tf_exp.txt" )
#inputFileNameList=( "/work/eg474423/ig440396_dendriticcells/exp/diffpeakdc/dc_up_input.txt"
#                    "/work/eg474423/ig440396_dendriticcells/exp/diffpeakdc/dc_down_input.txt"
#                    "/work/eg474423/ig440396_dendriticcells/exp/diffpeakdc/dc_up_input_h3k4me3.txt"
#                    "/work/eg474423/ig440396_dendriticcells/exp/diffpeakdc/dc_down_input_h3k4me3.txt"
#                    "/work/eg474423/ig440396_dendriticcells/exp/diffpeak/irf8_up_input.txt"
#                    "/work/eg474423/ig440396_dendriticcells/exp/diffpeak/irf8_down_input.txt" )
#outputLocationList=( "/work/eg474423/ig440396_dendriticcells/local/results/MotifStatistics/dc_up/"
#                     "/work/eg474423/ig440396_dendriticcells/local/results/MotifStatistics/dc_down/"
#                     "/work/eg474423/ig440396_dendriticcells/local/results/MotifStatistics/dc_up_h3k4me3/"
#                     "/work/eg474423/ig440396_dendriticcells/local/results/MotifStatistics/dc_down_h3k4me3/"
#                     "/work/eg474423/ig440396_dendriticcells/local/results/MotifStatistics/irf8_up/"
#                     "/work/eg474423/ig440396_dendriticcells/local/results/MotifStatistics/irf8_down/" )

etList=( "BCELL_UP" )
motifFileNameList=( $expdir"diffpeakdc/expression/ext/tfs_dc_b.txt" )
inputFileNameList=( $expdir"diffpeakdc/dc_b_up_input.txt" )
outputLocationList=( "/work/eg474423/ig440396_dendriticcells/local/results/MotifStatistics/BCELL_UP/" )

# Execution
for i in {1..$#etList}
do

    # Parameters
    et=$etList[$i]
    motifFileName=$motifFileNameList[$i]
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
        motif_list="-motif_list="$motifFileName
        gene_list="-gene_list="$geneFile
        #random_coordinates="-random_coordinates="
        #cobinding="-cobinding=2,3"
        output_location="-output_location="$outputLocation$coordName"/"

        # Running in cluster
        bsub -J $et"_"$coordName -o $et"_"$coordName"_out.txt" -e $et"_"$coordName"_err.txt" -W 100:00 -M 12000 -S 100 -P izkf -R "select[hpcwork]" ./motifStatistics_pipeline.zsh $coord_file $motif_list $gene_list $output_location 

    done
done


