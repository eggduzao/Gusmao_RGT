# Profiling the motif matching and enrichment

# Import
import os
import sys
import cProfile
from rgt.motifanalysis.Main import main

cProfile.run('main()',sort='time')


