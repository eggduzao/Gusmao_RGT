import os
import sys
import glob

logoList = [e.split("/")[-1][:-4] for e in glob.glob("./logo/*")]
print logoList
outFile = open("res.txt","w")
for fileName in glob.glob("./PWM/*"):
    print fileName.split("/")[-1][:-4]
    if(fileName.split("/")[-1][:-4] in logoList): outFile.write(fileName+"\n")
outFile.close()


