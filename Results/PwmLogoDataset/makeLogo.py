#################################################################################################
# Creates a logo representation of the given Position Frequency Matrix
#################################################################################################
params = []
params.append("###")
params.append("Input: ")
params.append("    1. resolution = The resolution of the resulting image. Eg. 300.")
params.append("    2. outExt = Extension of the output image. Eg. png or eps.")
params.append("    3. inputFileName = Name of the file representing the PWM.")
params.append("                       The file must be in JASPAR format.")
params.append("    4. outputLocation = Location of the output and temporary files.")
params.append("###")
params.append("Output: ")
params.append("    1. <inputFileName>.<outExt> = Figure of the logo.")
params.append("###")
#################################################################################################

# Import
import sys
from Bio import Motif
if(len(sys.argv) <= 1): 
    for e in params: print e
    sys.exit(0)

# Reading input
resolution = int(sys.argv[1])
outExt = sys.argv[2]
inputFileName = sys.argv[3]
outputLocation = sys.argv[4]
if(outputLocation[-1] != "/"): outputLocation+="/"

# File handling
inputFile = open(inputFileName,"r")
outName = inputFileName.split("/")[-1][:-4]

# Creating weblogo
pwm = Motif.read(inputFile,"jaspar-pfm")
pwm.weblogo(outputLocation+outName+".png")

# Termination
inputFile.close()

