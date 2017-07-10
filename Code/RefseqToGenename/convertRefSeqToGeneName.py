import os
import sys

# Create dicitonary of links
linkFile = open("/home/egg/Desktop/refseq_to_genename/refSeqToGeneName.txt","r")
linkDict = dict()
for line in linkFile:
    if(line[-1] == "\n"): line = line[:-1]
    ll = line.split("\t")
    if(len(ll[0]) == 0): r = "."
    else: r = ll[0]
    linkDict[ll[1]] = r
linkFile.close()

# Converting to new file
inFile = open("/home/egg/Desktop/refseq_to_genename/association_file_refseq.bed","r")
outFile = open("/home/egg/Desktop/refseq_to_genename/association_file.bed","w")
for line in inFile:
    ll = line.strip().split("\t")
    outFile.write("\t".join([ll[0],ll[1],ll[2],linkDict[ll[3]],ll[4],ll[5]])+"\n")
inFile.close()
outFile.close()


