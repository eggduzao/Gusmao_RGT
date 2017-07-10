import os
import sys
inFileName = "/home/egg/Desktop/FetchJaspar/pfm_vertebrates.txt"
outLoc = "/home/egg/Desktop/FetchJaspar/"
inFile = open(inFileName,"r")
outFile = None
for line in inFile:
    if(line[0] == ">"):
        if(outFile): outFile.close()
        ll = line[1:].strip().split(" ")
        outFile = open(outLoc+".".join(ll+["pwm"]),"w")
    else:
        ll = line.strip().split("\t")
        outFile.write(" ".join(ll)+"\n")
inFile.close()
outFile.close()

