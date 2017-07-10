import os
import sys
from copy import deepcopy
from rgt.GenomicRegion import *
from rgt.GenomicRegionSet import *
from rgt.Util import GenomeData, MotifData, AuxiliaryFunctions
from whoosh.index import create_in, open_dir
from whoosh.fields import Schema, NUMERIC, TEXT
from whoosh.qparser import QueryParser
from whoosh.analysis import StandardAnalyzer
from whoosh.query import Every, Term, And

class AnnotationSet:

    class GeneField:

        # Gff Fields 
        GENOMIC_REGION = 0
        ANNOTATION_SOURCE = 1
        FEATURE_TYPE = 2
        GENOMIC_PHASE = 3

        # Gtf Fields
        GENE_ID = 4
        TRANSCRIPT_ID = 5
        GENE_TYPE = 6
        GENE_STATUS = 7
        GENE_NAMES = 8
        TRANSCRIPT_TYPE = 9
        TRANSCRIPT_STATUS = 10
        TRANSCRIPT_NAME = 11
        LEVEL = 12

    def __init__(self, gene_source, tf_source=None, alias_source=None):

        self.schema=Schema(chr=TEXT(stored=True),
                      initial=NUMERIC(int,64,stored=True),
                      final=NUMERIC(int,64,stored=True),
                      score=NUMERIC(float,64,stored=True),
                      orientation=TEXT(stored=True),
                      annotation_source=TEXT(stored=True),
                      feature_type=TEXT(stored=True),
                      genomic_phase=TEXT(stored=True),
                      gene_id=TEXT(stored=True),
                      transcript_id=TEXT(stored=True),
                      gene_type=TEXT(stored=True),
                      gene_status=TEXT(stored=True),
                      gene_names=TEXT(stored=True),
                      transcript_type=TEXT(stored=True),
                      transcript_status=TEXT(stored=True),
                      transcript_name=TEXT(stored=True),
                      level=TEXT(stored=True))

        # Initializing Required Field - Gene List
        if(isinstance(gene_source,list)): # It can be a matrix - Used by internal methods.
            self.gene_list = gene_source
        if(isinstance(gene_source,str)): # It can be a string.
            if(os.path.isfile(gene_source)): # The string may represent a path to a gtf file.
                self.load_gene_list(gene_source)
            else: # The string may represent an organism which points to a gtf file within data.config.
                genome_data = GenomeData(gene_source)
                self.load_gene_list(genome_data.get_gencode_annotation())

    def load_gene_list(self, file_name, filter_havana=True):
 
        if(os.path.exists("index")): return "0"
        os.system("mkdir -p index")

        index = create_in("index", self.schema)
        writer = index.writer(procs=4, limitmb=512)

        # Opening GTF file
        try: gtf_file = open(file_name,"r")
        except Exception: pass # TODO

        # Reading GTF file
        for line in gtf_file:
        
            # Processing line
            line = line.strip()
            if(line[0] == "#"): continue
            line_list = line.split("\t")
            if(filter_havana and line_list[1] == "HAVANA"): continue
            addt_list = line_list[8].split(";")
            addt_list = filter(None,addt_list)

            # Processing additional list of options
            addt_dict = dict()
            for addt_element in addt_list:
                addt_element_list = addt_element.split(" ")
                addt_element_list = filter(None,addt_element_list)
                addt_element_list[1] = addt_element_list[1].replace("\"","") # Removing " symbol from string options
                addt_dict[addt_element_list[0]] = addt_element_list[1]
        
            # Removing dot from IDs
            addt_dict["gene_id"] = addt_dict["gene_id"].split(".")[0]
            addt_dict["transcript_id"] = addt_dict["transcript_id"].split(".")[0]
                
                                                                                                                                                                                          # Creating final version of additional arguments
            final_addt_list = []
            for addt_key in ["gene_id", "transcript_id", "gene_type", "gene_status", "gene_name", 
                             "transcript_type", "transcript_status", "transcript_name", "level"]:
                try: final_addt_list.append(addt_dict[addt_key])
                except Exception: final_addt_list.append(None)

            # Handling score
            current_score = 0
            if(AuxiliaryFunctions.string_is_int(line_list[5])):
                current_score = AuxiliaryFunctions.correct_standard_bed_score(line_list[5])

            # Creating GenomicRegion
            genomic_region = GenomicRegion(chrom = line_list[0], 
                                           initial = int(line_list[3])-1, 
                                           final = int(line_list[4]), 
                                           orientation = line_list[6], 
                                           data = current_score)

            # Creating final vector
            final_vector = [genomic_region,line_list[1],line_list[2],line_list[7]] + final_addt_list

            # Writing data
            writer.add_document(chr=unicode(line_list[0]),
                      initial=int(line_list[3])-1,
                      final=int(line_list[4]),
                      score=unicode(current_score),
                      orientation=unicode(line_list[6]),
                      annotation_source=unicode(line_list[1]),
                      feature_type=unicode(line_list[2]),
                      genomic_phase=unicode(line_list[7]),
                      gene_id=unicode(final_addt_list[0]),
                      transcript_id=unicode(final_addt_list[1]),
                      gene_type=unicode(final_addt_list[2]),
                      gene_status=unicode(final_addt_list[3]),
                      gene_names=unicode(final_addt_list[4]),
                      transcript_type=unicode(final_addt_list[5]),
                      transcript_status=unicode(final_addt_list[6]),
                      transcript_name=unicode(final_addt_list[7]),
                      level=unicode(final_addt_list[8]))
            
        # Termination
        gtf_file.close()
        writer.commit()

    def test(self):

        index = open_dir("index")
        resDict = []
        with index.searcher() as searcher:
            query_parser = QueryParser("feature_type", index.schema)
            query = query_parser.parse(u"gene")
            results = searcher.search(query, limit=None, scored=False, sortedby=None)
            for e in results: resDict.append(e["initial"])
        print len(resDict)

    def get_promoters(self, promoterLength=1000, gene_set = None):
        """
        Gets promoters of genes given a specific promoter length.
        It returns a GenomicRegionSet with such promoters. The ID of each gene will be put
        in the NAME field of each GenomicRegion. Each promoter includes also the coordinate of
        the 5' base pair, therefore each promoter actual length is promoterLength+1.

        Keyword arguments:
        promoterLength -- The length of the promoter region.
        gene_set -- A set of genes to narrow the search.

        Return:
        result_grs -- A GenomicRegionSet containing the promoters.
        unmapped_gene_list -- A list of genes that could not be mapped to an ENSEMBL ID.
        """

        # Fetching gene names
        mapped_gene_list = None
        unmapped_gene_list = None
        if(gene_set): mapped_gene_list, unmapped_gene_list = self.fix_gene_names(gene_set)
        
        index = open_dir("index")

        # Creating GenomicRegionSet
        result_grs = GenomicRegionSet("promoters")
        with index.searcher() as searcher:
            query_parser = QueryParser("feature_type", index.schema)
            query = query_parser.parse(u"gene")
            results = searcher.search(query, limit=None, scored=False, sortedby=None)
            for e in results:
                orientation = e["orientation"]
                if(orientation == "+"):
                    final = e["initial"] + 1
                    initial = e["initial"] - promoterLength
                else:
                    initial = e["final"] - 1
                    final = e["final"] + promoterLength + 1
                result_grs.add(GenomicRegion(chrom = e["chr"], 
                                         initial = initial, 
                                         final = final,
                                         name = e["gene_id"],
                                         orientation = orientation, 
                                         data = e["score"]))
        if(gene_set): return result_grs, unmapped_gene_list
        else: return result_grs

if __name__ == "__main__":

    a = AnnotationSet("/home/egg/Projects/RGT/Results/Usage/RGT_MotifAnalysis/Installation/rgtdata/hg19/test2.gtf")
    a.get_promoters()


