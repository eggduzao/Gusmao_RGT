
# Import
from rgt.AnnotationSet import AnnotationSet
from rgt.GeneSet import GeneSet

#a = AnnotationSet("hg19",alias_source="hg19")
a = AnnotationSet("/home/egg/Projects/RGT/Results/Usage/RGT_MotifAnalysis/Installation/rgtdata/hg19/test2.gtf")

p = a.get_promoters()

#qd1 = dict([(a.GeneField.FEATURE_TYPE,"gene")])
#qa1 = a.get(qd1)

#for qa in qa1.gene_list:
#  print qa[a.GeneField.GENOMIC_REGION]

#print "--------------"

#gs = GeneSet("gs")
#gs.genes = ["ENSG00000223972","PLEKHN1","SAMD11","GABP","OR4F16"]

#prom = a.get_promoters(promoterLength=1000,gene_set=gs)
#prom = a.get_promoters(promoterLength=1000)
#for gr in prom[0]: print gr

#print "--------------"

#exons = a.get_exons()
#for gr in exons: print gr



