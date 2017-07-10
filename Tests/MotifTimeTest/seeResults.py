import os
import sys
from operator import itemgetter
inFile = open("./result.txt","r")
l1 = "a"
res = []
while l1:
    l1 = inFile.readline()
    l2 = inFile.readline()
    if(l1 and l2):
        res.append([l1.strip().split("/")[-1],float(l2.strip())])
inFile.close()

res = sorted(res, key=itemgetter(1))

for e in res: print e


