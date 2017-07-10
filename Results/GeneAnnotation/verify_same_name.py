
# Import
import os
import sys

# Input
inLoc = "./"
inList = [inLoc+"hg/alias.txt", inLoc+"mm/alias.txt"]

# Iterating on inputList:
for inFileName in inList:

  outLoc = "/".join(inFileName.split("/")[:-1])+"/"
  outFileName = outLoc+"report.txt"
  outFile = open(outFileName,"w")

  # Verifying if all IDs are different
  outFile.write("### Test1:\n")
  inFile = open(inFileName,"r")
  myDict = dict(); counter = 0
  for line in inFile:
    ll = line.strip().split("\t")
    try:
      a = myDict[ll[0]]
      outFile.write(ll[0]+"\n")
    except Exception: myDict[ll[0]] = None
    counter += 1
  inFile.close()
  outFile.write("\n")

  # Verifying if there are two equal names for different IDs
  outFile.write("### Test2:\n")
  inFile = open(inFileName,"r")
  myDict = dict()
  for line in inFile:
    ll = line.strip().split("\t")
    vec = ll[2].split("&")
    for e in vec:
      try:
        a = myDict[e]
        outFile.write("\t".join([e,a,ll[0]])+"\n")
      except Exception: myDict[e] = ll[0]
  inFile.close()
  outFile.close()


