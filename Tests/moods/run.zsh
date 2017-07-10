#!/bin/zsh

# Parameters
mLoc="/home/egg/Desktop/moods/moods/"
bLoc="/home/egg/Desktop/moods/bio/"
inLoc="/home/egg/Projects/RGT/reg-gen/data/motifs/jaspar_vertebrates/"
#motifList=( "MA0002.2.RUNX1" "MA0003.2.TFAP2A" "MA0004.1.Arnt" "MA0006.1.Arnt::Ahr" "MA0007.2.AR" "MA0009.1.T" "MA0014.2.PAX5" "MA0017.1.NR2F1" "MA0018.2.CREB1" "MA0019.1.Ddit3::Cebpa" "MA0024.2.E2F1" "MA0025.1.NFIL3" "MA0027.1.En1" "MA0028.1.ELK1" "MA0029.1.Mecom" "MA0030.1.FOXF2" "MA0031.1.FOXD1" "MA0032.1.FOXC1" "MA0033.1.FOXL1" "MA0035.3.Gata1" "MA0036.2.GATA2" "MA0037.2.GATA3" "MA0038.1.Gfi1" "MA0039.2.Klf4" "MA0040.1.Foxq1" "MA0041.1.Foxd3" "MA0042.1.FOXI1" "MA0043.1.HLF" "MA0046.1.HNF1A" "MA0047.2.Foxa2" "MA0048.1.NHLH1" "MA0050.2.IRF1" "MA0051.1.IRF2" "MA0052.2.MEF2A" "MA0056.1.MZF1_1-4" "MA0057.1.MZF1_5-13" "MA0058.2.MAX" "MA0059.1.MYC::MAX" "MA0060.2.NFYA" "MA0062.2.GABPA" "MA0063.1.Nkx2-5" "MA0065.2.PPARG::RXRA" "MA0066.1.PPARG" "MA0067.1.Pax2" "MA0068.1.Pax4" "MA0069.1.Pax6" "MA0070.1.PBX1" "MA0071.1.RORA_1" "MA0072.1.RORA_2" "MA0073.1.RREB1" "MA0074.1.RXRA::VDR" "MA0075.1.Prrx2" "MA0076.2.ELK4" "MA0077.1.SOX9" "MA0078.1.Sox17" "MA0079.3.SP1" "MA0080.3.Spi1" "MA0081.1.SPIB" "MA0083.2.SRF" "MA0084.1.SRY" )
motifList=( "MA0003.2.TFAP2A" "MA0002.2.RUNX1" )

# Execution
#for m in $motifList
#do
  #python moods_vs_bio.py $inLoc$m".pwm"
#done

python multimoods.py $inLoc $motifList

#python moods_vs_multimoods.py $inLoc $motifList


