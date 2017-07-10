
# _format = removed random contigs and chrY by:
# grep -v random 
# grep -v chrY

# Import
import os
import sys

# Input
inLoc = "/home/egg/Projects/RGT/Results/ExcludedRegions/"
inList = ["blacklist_hg19_duke_format", "blacklist_hg19_kundaje_format", "blacklist_mm9_kundaje_format"]
genSizeDict = dict([("hg19",3036303846),("mm9",2639016663)])

# Execution
for inName in inList:
  organism = inName.split("_")[1]
  inFileName = inLoc+inName+".bed"
  inFile = open(inFileName,"r")
  summ = 0
  for line in inFile:
    ll = line.strip().split("\t")
    summ += int(ll[2]) - int(ll[1])
  inFile.close()
  print inName+"\t"+str(round(100.0*(float(summ)/float(genSizeDict[organism])),4))


