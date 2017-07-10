import os
import sys

inFileName = sys.argv[1]
outLoc = sys.argv[2]
outEvName = outLoc+"mpbs_ev.bed"
outNevName = outLoc+"mpbs_nev.bed"
outRandName = outLoc+"mpbs_rand.bed"

inFile = open(inFileName,"r")
outEv = open(outEvName,"w")
outNev = open(outNevName,"w")
outRand = open(outRandName,"w")
for line in inFile:
  ll =line.strip().split("\t")
  if(ll[8] == "0,0,0"): outRand.write(line)
  elif(ll[8] == "130,0,0"): outNev.write(line)
  elif(ll[8] == "0,130,0"): outEv.write(line)
inFile.close()
outEv.close()
outNev.close()
outRand.close()


