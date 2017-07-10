import os
import sys
inFile = open("/home/egg/Desktop/refseq_to_genename/association_file_sort.bed","r")
outFile = open("/home/egg/Desktop/refseq_to_genename/association_file.bed","w")
tpl = []
for line in inFile:
    ll = line.strip().split("\t")
    if(len(tpl) == 0):
        tpl.append(ll)
        continue
    if("\t".join(tpl[-1])+"\n" == line): pass
    elif(tpl[-1][0] == ll[0] and tpl[-1][1] == ll[1] and tpl[-1][2] == ll[2]):
        if(tpl[-1][3] == "."): tpl[-1][3] = ll[3]
        elif(ll[3] != "."): tpl.append(ll)
    else: tpl.append(ll)
for e in tpl: outFile.write("\t".join(e)+"\n")
inFile.close()
outFile.close()
