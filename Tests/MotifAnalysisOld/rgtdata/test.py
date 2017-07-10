
import time
from rgt.AnnotationSet import GeneAnnotationSet
from rgt.Util import AnnotationField

t1 = time.time()
ann = GeneAnnotationSet("/home/egg/Projects/SVN/reg-gen/data/hg19/teste.gtf")
#ann = GeneAnnotationSet("/home/egg/Projects/SVN/reg-gen/data/hg19/gencode_annotation.gtf")

"""
t2 = time.time()
ann2 = ann.subset_comp(AnnotationField.FEATURE_TYPE,"gene")
t3 = time.time()
ann3 = ann.subset_fil(AnnotationField.FEATURE_TYPE,"gene")
t4 = time.time()
ann4 = ann.subset_np(AnnotationField.FEATURE_TYPE,"gene")
t5 = time.time()
"""

"""
for e in ann2.annotation_list: print e[AnnotationField.TRANSCRIPT_ID]
print "--"
for e in ann3.annotation_list: print e[AnnotationField.TRANSCRIPT_ID]
print "--"
for e in ann4.annotation_list: print e[AnnotationField.TRANSCRIPT_ID]
"""

"""
print t2-t1
print t3-t2
print t4-t3
print t5-t4
"""

def dostf(test):
  annT = ann.multiple_subset2(AnnotationField.FEATURE_TYPE,test)
  for e in annT.annotation_list:
    if(e): print e[AnnotationField.TRANSCRIPT_ID]
    else: print "None"
  print "--"

  annT.annotation_list[0][AnnotationField.TRANSCRIPT_ID] = 11
  print annT.annotation_list[0][AnnotationField.TRANSCRIPT_ID]
  print ann.annotation_list[0][AnnotationField.TRANSCRIPT_ID]

test = ["gene"]
dostf(test)


"""
test = ["gene","exon"]
dostf(test)

test = ["1","2","3","4","5","6","7","8","9"]
dostf(test)

test = ["9","9","9"]
dostf(test)

test = ["9","1","8","9","9"]
dostf(test)

test = ["8"]
dostf(test)

test = ["1"]
dostf(test)

test = ["7","8","1","3"]
dostf(test)

test = ["1","2"]
dostf(test)

test = ["9","10","11","3","4"]
dostf(test)

test = ["2","6","8"]
dostf(test)
"""

"""
t2 = time.time()
ann2 = ann.multiple_subset1(AnnotationField.FEATURE_TYPE,["gene","exon","start_codon"]+["test"]*1000)
t3 = time.time()
ann2 = ann.multiple_subset2(AnnotationField.FEATURE_TYPE,["gene","exon","start_codon"]+["test"]*1000)
t4 = time.time()

print t2-t1
print t3-t2
print t4-t3
"""

