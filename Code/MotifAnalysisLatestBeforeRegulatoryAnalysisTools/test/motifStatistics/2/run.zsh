#!/bin/zsh

coordFileName="/work/eg474423/ig440396_dendriticcells/exp/motifanalysis/test/motifStatistics/2/coordinates.bed"
motifFileName="/work/eg474423/ig440396_dendriticcells/exp/motifanalysis/test/motifStatistics/2/motifList.txt"
geneFileName="/work/eg474423/ig440396_dendriticcells/exp/diffpeak/exp/irf8_up_genes_1.7.txt"
outputLocation="/work/eg474423/ig440396_dendriticcells/exp/motifanalysis/test/motifStatistics/2/out/"

motifStatistics $coordFileName $motifFileName $geneFileName $outputLocation


