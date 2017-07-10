a = open("/home/egg/Projects/RGT/Tests/moods/res2.txt","r")
s = 0.0
for line in a:
  ll = line.strip().split("\t")
  s+=float(ll[1])
print s
a.close()
