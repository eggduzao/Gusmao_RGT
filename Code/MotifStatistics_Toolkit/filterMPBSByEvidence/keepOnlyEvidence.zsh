#!/bin/zsh

cs="/home/egg/Desktop/MotifStatistics_Toolkit/filterMPBSByEvidence/mm9.chrom.sizes"
il="/home/egg/Desktop/MotifStatistics_Toolkit/filterMPBSByEvidence/"
folderList=( "cDC_m_PU1_IRF8__irf8_paper_genes" "cDC_PU1_IRF8__irf8_paper_genes" "cDC_PU1_m_IRF8__irf8_paper_genes"
             "CDP_m_PU1_IRF8__irf8_paper_genes" "CDP_PU1_IRF8__irf8_paper_genes" "CDP_PU1_m_IRF8__irf8_paper_genes"
             "pDC_m_PU1_IRF8__irf8_paper_genes" "pDC_PU1_IRF8__irf8_paper_genes" "pDC_PU1_m_IRF8__irf8_paper_genes" )

for inFolder in $folderList
do

  inF=$il$inFolder"/"

  bigBedToBed $inF"mpbs.bb" $inF"mpbs.bed"
  python splitEvNevRand.py $inF"mpbs.bed" $inF
  rm $inF"mpbs.bb" $inF"mpbs.bed"
  
  cat $inF"mpbs_ev.bed" $inF"mpbs_nev.bed" > $inF"mpbs_raw.bed"
  sort -k1,1 -k2,2n $inF"mpbs_raw.bed" > $inF"mpbs.bed"
  bedToBigBed $inF"mpbs.bed" $cs $inF"mpbs.bb" -verbose=0
  
  rm $inF"mpbs_raw.bed" $inF"mpbs.bed" $inF"mpbs_rand.bed" $inF"mpbs_ev.bed" $inF"mpbs_nev.bed"
done


