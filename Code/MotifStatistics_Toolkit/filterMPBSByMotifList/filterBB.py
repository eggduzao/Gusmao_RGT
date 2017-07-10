
# Import
import os
import sys

# Input
factorFileName = "/home/egg/Desktop/FilterBB/tfList.txt"
csFileName = "/home/egg/Desktop/FilterBB/mm9.chrom.sizes"
inLoc = "/home/egg/Desktop/FilterBB/"
inList = ["CDP_IRF8_DOWN","CDP_IRF8_UP","CDP_PU1_DOWN","CDP_PU1_IRF8_DOWN","CDP_PU1_IRF8_UP","CDP_PU1_UP"]

# Reading tf list
tfFile = open(factorFileName,"r")
tfVec = []
for line in tfFile:
  tfVec.append(line.strip())
tfFile.close()

# Iterating in bb list
for inFileName in inList:

  # Parameters
  bbFileName = inLoc+inFileName+".bb"
  bedFileNameTemp = inLoc+inFileName+"_temp.bed"
  bedFileNameFiltered = inLoc+inFileName+".bed"
  bbFilteredFileName = inLoc+inFileName+"_filt.bb"

  # Converting to bed
  os.system("bigBedToBed "+bbFileName+" "+bedFileNameTemp)

  # Filtering
  bedFile = open(bedFileNameTemp,"r")
  outFile = open(bedFileNameFiltered,"w")
  for line in bedFile:
    ll = line.strip().split("\t")
    if(ll[3] in tfVec): outFile.write(line)
  bedFile.close()
  outFile.close()

  # Converting to bb
  os.system("bedToBigBed "+bedFileNameFiltered+" "+csFileName+" "+bbFilteredFileName+" -verbose=0")
  os.system(" ".join(["rm",bbFileName,bedFileNameTemp,bedFileNameFiltered]))


