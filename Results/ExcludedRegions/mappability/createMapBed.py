
# Import
import os
import sys
from bx.bbi.bigwig_file import BigWigFile
lib_path = "/work/eg474423/eg474423_Projects/trunk/TfbsPrediction/Code"
sys.path.append(lib_path)
from util import *

# Input
inFileName = sys.argv[1]
csFileName = sys.argv[2]
outFileName = sys.argv[3]

# Parameters
regionLen = 100000
mapThresh = 0.25 # Allows for 4 reads

# Reading csDict
csDict = dict()
csFile = open(csFileName,"r")
for line in csFile:
  ll = line.strip().split("\t")
  csDict[ll[0]] = int(ll[1])
csFile.close()
chrList = sorted(csDict.keys())

# Opening files
inFile = open(inFileName,"r")
bw = BigWigFile(inFile)
outFile = open(outFileName,"w")

# Iterating over chromosomes
for chrName in chrList:

  # Initialization
  lastPos = 0
  flag = False
  
  # Tiled iteration
  for i in range(0,csDict[chrName],regionLen): 
    p1 = i
    p2 = min(i+regionLen,csDict[chrName])
    signal = aux.correctBW(bw.get(chrName,p1,p2),p1,p2)
    for j in range(0,len(signal)):
      if(flag):
        if(signal[j] >= mapThresh):
          outFile.write("\t".join([chrName,str(lastPos),str(p1+j)])+"\n")
          flag = False
      else:
        if(signal[j] < mapThresh):
          lastPos = p1+j
          flag = True
  if(flag):
    outFile.write("\t".join([chrName,str(lastPos),str(csDict[chrName])])+"\n")
    flag = False

# Termination
inFile.close()
outFile.close()


