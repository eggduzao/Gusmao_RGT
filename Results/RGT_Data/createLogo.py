
import os
import sys
import glob
from Bio import Motif

inPath = "/home/egg/work/eg474423/reg-gen/data/motifs/jaspar_vertebrates/"
outPath = "/home/egg/work/eg474423/reg-gen/data/logos/jaspar_vertebrates/"

for inputFileName in glob.glob(inPath+"*.pwm"):

  inputFile = open(inputFileName,"r")
  outName = ".".join(inputFileName.split("/")[-1].split(".")[:-1])
  pwm = Motif.read(inputFile,"jaspar-pfm")
  pwm.weblogo(outPath+outName+".png", res=300, format="PNG")
  inputFile.close()

