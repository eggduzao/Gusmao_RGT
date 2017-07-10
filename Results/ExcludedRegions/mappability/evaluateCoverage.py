
# Import
import os
import sys

# Input
inLoc = "/work/eg474423/eg474423_Projects/trunk/RGT/Results/ExcludedRegions/mappability/"
inList = ["hg19_map4_filter_50", "mm9_map4_filter_50"]
genSizeDict = dict([("hg19",3036303846),("mm9",2639016663)])

# Execution
for inName in inList:
  organism = inName.split("_")[0]
  inFileName = inLoc+inName+".bed"
  inFile = open(inFileName,"r")
  summ = 0
  for line in inFile:
    ll = line.strip().split("\t")
    summ += int(ll[2]) - int(ll[1])
  inFile.close()
  print inName+"\t"+str(round(100.0*(float(summ)/float(genSizeDict[organism])),4))


