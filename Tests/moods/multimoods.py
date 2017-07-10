
# Import
import os
import sys
import MOODS
from Bio import motifs
from Bio.Seq import Seq
from os.path import basename
from time import time

# Input
input_loc = sys.argv[1]
motif_list = sys.argv[2:]
pseudocounts = 0.1
background = {'A':0.25,'C':0.25,'G':0.25,'T':0.25}
precision = 10000
fpr = 0.0001

# Parameters
seqFile = open("seq.txt","r")
seq = seqFile.readline().strip().upper()
seq = "NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN"
seq = seq * 100000000
seqFile.close()
inName = "results3"

# Creating PSSM
pssm_list = []
for input_file_name in [input_loc+m+".pwm" for m in motif_list]:
  name = ".".join(basename(input_file_name).split(".")[:-1])
  input_file = open(input_file_name,"r")
  pfm = motifs.read(input_file, "pfm")
  motif_len = len(pfm)
  pwm = pfm.counts.normalize(pseudocounts)
  input_file.close()
  pssm = pwm.log_odds(background)
  pssm_list.append([pssm[e] for e in ["A","C","G","T"]])

# Thresholds
fpr_file_name = "/".join(input_loc.split("/")[:-2])+"/"+input_loc.split("/")[-2]+".fpr"
tdict = dict()
fpr_file = open(fpr_file_name,"r")
header = fpr_file.readline()
fpr_values = [float(e) for e in header.strip().split("\t")[1:]]
for line in fpr_file:
  ll = line.strip().split("\t")
  tdict[ll[0]] = dict()
  for i in range(1,len(ll)): tdict[ll[0]][fpr_values[i-1]] = float(ll[i]) 
fpr_file.close()
threshlist = [tdict[e][fpr] for e in motif_list]

t1 = time()

moodsBedFileName = "./multimoods/"+inName
moodsBed = open(moodsBedFileName+".bed","w")
counter = 0
for r in MOODS.search(seq, pssm_list, threshlist, absolute_threshold=True, both_strands=True, algorithm="lf"):
  counter += 1
  print counter
  for (position, score) in r:
    if(position >= 0):
      p1 = position
      strand = "+"
    else:
      p1 = -position
      strand = "-"
    p2 = p1 + motif_len
    moodsBed.write("\t".join(["chr1",str(p1),str(p2),inName,str(int(score)),strand])+"\n")
moodsBed.close()

t2 = time()

print "\t".join([str(e) for e in [inName,round(t2-t1,4)]])

# Bed merging and sorting
#os.system("sort -k1,1 -k2,2n "+moodsBedFileName+"_t1.bed > "+moodsBedFileName+"_t2.bed")
#os.system("bedtools merge -i "+moodsBedFileName+"_t2.bed > "+moodsBedFileName+".bed")
#os.system("rm "+moodsBedFileName+"_t1.bed "+moodsBedFileName+"_t2.bed")


