import os
import sys

outLoc = "/home/egg/Projects/RGT/Results/FetchJaspar/motifs/"
inFile = open("/home/egg/Projects/RGT/Results/FetchJaspar/pfm_vertebrates.txt", "r")
outFile = None
for line in inFile:

  if(line[0] == ">"):
    if(outFile): outFile.close()
    ll = line[1:].strip().split("\t")
    outFile = open(outLoc+ll[0]+"."+ll[1]+".pwm","w")

  elif(line[0] in ["A", "C", "G", "T"]):
    ll = line.strip().translate(None, "ACGT[]").split(" ")
    newline = " ".join([x for x in ll if x])
    outFile.write(newline+"\n")

  else: continue

inFile.close()

