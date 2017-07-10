
# Import
import os
import sys
import glob
import time

# Input
pwmLoc="/work/eg474423/reg-gen/data/PWM/"
genomeFile="/hpcwork/izkf/projects/egg/MotifTest/genome.fa"
csFile="/hpcwork/izkf/projects/egg/MotifTest/chrom.sizes"
outputLocation="/hpcwork/izkf/projects/egg/MotifTest/out/"
outputFileName="/hpcwork/izkf/projects/egg/MotifTest/result.txt"

# Parameters
searchMethod="biopython"
scoringMethod="fpr"
pseudoC="0.00"
fprValue="0.0001"
precValue="10000"

# Factor Loop
outputFile = open(outputFileName,"w")
for factorFileName in glob.glob(pwmLoc+"*.pwm"):

  factorName = ".".join(factorFileName.split("/")[-1].split(".")[:-1])
    
  # Parameters
  pwm_list="-pwm_list="+factorFileName
  genome_list="-genome_list="+genomeFile

  chrom_sizes_file="-chrom_sizes_file="+csFile
  organism="-organism=egg"
  search_method="-search_method="+searchMethod
  scoring_method="-scoring_method="+scoringMethod
  pseudocounts="-pseudocounts="+pseudoC
  #bitscore="-bitscore="
  fpr="-fpr="+fprValue
  precision="-precision="+precValue
  #high_cutoff="-high_cutoff="
  #functional_depth="-functional_depth="
  #fimo_thresold="-fimo_thresold="

  output_location="-output_location="+outputLocation
  bigbed="-bigbed=N"
  print_mpbs="-print_mpbs=Y"
  print_graph_mmscore="-print_graph_mmscore=N"

  paramVec = [ pwm_list, genome_list, chrom_sizes_file, organism, search_method, scoring_method,
               pseudocounts, fpr, precision, output_location, bigbed, print_mpbs, print_graph_mmscore ]

  #t1 = time.clock()
  os.system("rgt-motifanalysis matching "+" ".join(paramVec))
  #t2 = time.clock()
  #size = 0.0
  #outFN = outputLocation+factorName
  #if(os.path.isfile(outFN)): size = os.path.getsize(outFN)
  #outputFile.write("\t".join([factorFileName,str(t2-t1),str(float(size)/float(1000000))])+"\n")
  #print "Size: "+str(float(size)/1000000.0)+"\n-------------------------------------\n"

outputFile.close()


