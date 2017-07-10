
# Import
import os
import sys
import MOODS
from Bio import motifs
from Bio.Seq import Seq
from os.path import basename
from time import time

# Input
input_file_name = sys.argv[1]
pseudocounts = 0.1
background = {'A':0.25,'C':0.25,'G':0.25,'T':0.25}
precision = 10000
fpr = 0.0001

# Parameters
seqFile = open("seq.txt","r")
seq = seqFile.readline().strip().upper()
seq = seq * 100
seqFile.close()
inName = ".".join(input_file_name.split("/")[-1].split(".")[:-1])

# Creating PSSM
name = ".".join(basename(input_file_name).split(".")[:-1])
input_file = open(input_file_name,"r")
pfm = motifs.read(input_file, "pfm")
motif_len = len(pfm)
pwm = pfm.counts.normalize(pseudocounts)
input_file.close()
pssm = pwm.log_odds(background)
pssm_list = [pssm[e] for e in ["A","C","G","T"]]

# Thresholds
input_loc = "/".join(input_file_name.split("/")[:-1])+"/"
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
threshold = tdict[inName][fpr]

t1 = time()

moodsBedFileName = "./moods/"+inName
moodsBed = open(moodsBedFileName+"_t1.bed","w")
for r in MOODS.search(seq,[pssm_list], threshold, absolute_threshold=True, both_strands=True):
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

"""
curr_seq = Seq(seq, pssm.alphabet)
bioBedFileName = "./bio/"+inName
bioBed = open(bioBedFileName+"_t1.bed","w")
for position, score in pssm.search(curr_seq, threshold=threshold):
  if(position >= 0):
    p1 = position
    strand = "+"
  else:
    p1 = len(seq) + position
    strand = "-"
  p2 = p1 + motif_len
  bioBed.write("\t".join(["chr1",str(p1),str(p2),inName,str(int(score)),strand])+"\n")

bioBed.close()
t3 = time()
"""

#print "\t".join([str(e) for e in [inName,round(t2-t1,4),round(t3-t2,4)]])
print "\t".join([str(e) for e in [inName,round(t2-t1,4)]])

# Bed merging and sorting
os.system("sort -k1,1 -k2,2n "+moodsBedFileName+"_t1.bed > "+moodsBedFileName+"_t2.bed")
os.system("bedtools merge -i "+moodsBedFileName+"_t2.bed > "+moodsBedFileName+".bed")
#os.system("sort -k1,1 -k2,2n "+bioBedFileName+"_t1.bed > "+bioBedFileName+"_t2.bed")
#os.system("bedtools merge -i "+bioBedFileName+"_t2.bed > "+bioBedFileName+".bed")
os.system("rm "+moodsBedFileName+"_t1.bed "+moodsBedFileName+"_t2.bed")
#os.system("rm "+moodsBedFileName+"_t1.bed "+moodsBedFileName+"_t2.bed "+bioBedFileName+"_t1.bed "+bioBedFileName+"_t2.bed")


