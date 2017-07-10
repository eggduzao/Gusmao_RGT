#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
%prog [options] <BAM>

Peak Caller for a single ChIP-seq signal.

The first argument gives the ChIP-seq BAM file, the second 
argument the input-DNA control BAM file.

Copyright (C) 2016  Manuel Allhoff (allhoff@aices.rwth-aachen.de)

This program comes with ABSOLUTELY NO WARRANTY. This is free 
software, and you are welcome to redistribute it under certain 
conditions. Please see LICENSE file for details.
"""

from __future__ import print_function
from optparse import OptionParser
import sys
from rgt.CoverageSet import CoverageSet
from rgt.GenomicRegionSet import GenomicRegionSet
from rgt.GenomicRegion import GenomicRegion
from rgt.Util import GenomeData
from rgt.ODIN.get_extension_size import get_extension_size
from rgt.helper import get_chrom_sizes_as_genomicregionset
from scipy.stats import binom_test
from numpy import sum, mean

class HelpfulOptionParser(OptionParser):
    """An OptionParser that prints full help on errors."""
    def error(self, msg):
        self.print_help(sys.stderr)
        self.exit(2, "\n%s: error: %s\n" % (self.get_prog_name(), msg))

def filter_cov(c, overall_cov, theshold=0.05, min_cov=10):
    """Evaluate significance of coverage c"""
    p = 1

    if c > min_cov:
        s = sum(overall_cov)
        empirical_p = mean(overall_cov[overall_cov > 0]) / s
        p = binom_test((c, s-c), p=empirical_p)
    
    return True if p < theshold else False

if __name__ == '__main__':
    #parse input
    parser = HelpfulOptionParser(usage=__doc__)
        
    parser.add_option("--prefix", dest="prefix", default=None, help="prefix for all created files")
    (options, args) = parser.parse_args()
     
    i = 2
    if len(args) != i:
        parser.error("Exactly %s parameters are needed" %i)
     
    bamfile = args[0]
    bamfile_input_dna = args[1]
    
    ##### Step 1: Preprocessing
    #read chromosome sizes
    g = GenomeData('mm9')
    regionset = get_chrom_sizes_as_genomicregionset(g.get_chromosome_sizes())
    
    #compute extension size
    ext, _ = get_extension_size(bamfile, start=0, end=300, stepsize=5)
    
    #create CoverageSets
    cov = CoverageSet('IP coverage', regionset)
    cov.coverage_from_bam(bam_file=bamfile, read_size=ext)
    
    cov_input = CoverageSet('input-dna coverage', regionset)
    cov_input.coverage_from_bam(bam_file=bamfile_input_dna, read_size=0)
    
    #normalize ChIP-seq signal
    cov.norm_gc_content(cov_input.coverage, g.get_genome(), g.get_chromosome_sizes())
    cov.subtract(cov_input)
    
    ##### Step 2: Peak Calling
    res = GenomicRegionSet('res')
    
    for i, el in enumerate(cov.overall_cov):
        if filter_cov(el, cov.overall_cov):
            chrom, s, e = cov.index2coordinates(i, regionset)
            res.add(GenomicRegion(chrom, s, e+1))
        
    res.merge()
        
    ##### Step 3: Postprocessing
    res.write_bed(options.prefix + '_peaks.bed')
    cov.write_bigwig(options.prefix + '_signal.bw', g.get_chromosome_sizes())
    