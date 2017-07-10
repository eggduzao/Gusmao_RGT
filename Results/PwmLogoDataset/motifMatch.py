import sys
import os
import math
import pylab
import matplotlib.pyplot as plt
from Bio import Motif
from Bio.Seq import Seq

# Motif matching
pwm = Motif.read(open("irf8.pfm"),"jaspar-pfm")
sd = Motif.ScoreDistribution(pwm,precision=10000)
print sd.threshold_fpr(0.001)
print sd.threshold_fpr(0.0001)
print sd.threshold_fpr(0.00001)
sequence = Seq("TATCTTTGAAACCGAAACTACTATCCTGAAGCCGAAACTGC")
scoreVec = []
flagF = True
for pos, score in pwm.search_pwm(sequence,threshold=-1000.0):
    if(pos == 0 and flagF):
        scoreVec.append(score)
        flagF = False
    if(pos > 0): scoreVec.append(score)

# Removing background
for i in range(0,len(scoreVec)): scoreVec[i] = (((scoreVec[i]-min(scoreVec))/(max(scoreVec)-min(scoreVec))) * max(scoreVec) ) + 0.0
print scoreVec

# PWM
#def pwmFun(M):
#    for j in range(0,len(M[0])):
#        total = 0
#        for i in range(0,len(M)):
#            total += M[i][j]
#        H = 0
#        for i in range(0,len(M)):
#            freq = M[i][j] / total
#            logFreq = math.log(freq,2)
#            H -= freq * logFreq
#        R = 2-H
#        for i in range(0,len(M)):
#            freq = M[i][j] / total
#            M[i][j] = R * freq
#    return M

# Read PWM
#inFile = open("irf8.pfm","r")
#pwm = []
#for line in inFile:
#    ll = line.strip().split(" ")
#    pwm.append([float(e)+0.01 for e in ll])
#inFile.close()
#pwm = pwmFun(pwm)
#nuc = ["A","C","G","T"]
#pwmD = dict([(nuc[i],pwm[i]) for i in range(0,len(nuc))])

# Create score vector
#sequence = "TAGATTTAAAATCGAAACTAAAGATCCTAAAACCGAAACTGC"
#scoreVec = []
#for i in range(0,len(sequence)-len(pwm)):
#    score = 0
#    for j in range(0,len(pwm)): score += pwmD[sequence[i+j]][j]
#    scoreVec.append(score)

# Creating figure
fig = plt.figure(figsize=(8,5), facecolor='w', edgecolor='k')
ax = fig.add_subplot(111)
ax.plot(range(0,len(scoreVec)), scoreVec)
ax.set_xlabel("Genome Position (bp)")
ax.set_ylabel("Motif Match Score")
pylab.xlim([0,len(scoreVec)-1])
fig.savefig("./irf8_mmscore.png", format="png", dpi=300, bbox_inches='tight') 


