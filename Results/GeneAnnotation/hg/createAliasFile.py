# This script takes a hgnc annotation and create an alias.txt file for the human genome

# Import
import os
import sys

# Input
inFileName = "./hgnc_complete_set.txt"
outFileName = "./alias.txt"

# Iterating over input file
inFile = open(inFileName,"r")
outFile = open(outFileName,"w")
inFile.readline()
for line in inFile:

  ll = line[:-1].split("\t")

  # Ensembl ID
  ens_id = ll[18]
  if(not ens_id): continue
  
  # Official Symbol
  official_symbol = ll[1]

  # Symbols = HGNC ID, Official Symbol, Previous Symbols, Synonyms, Accession Numbers, Enzyme IDs, Entrez Gene ID,
  #           RefSeq IDs, CCDS IDs, VEGA IDs, OMIM ID (supplied by NCBI), UniProt ID (supplied by UniProt), UCSC ID (supplied by UCSC)
  symbols = [e.upper() for e in ll[0].split(", ")] + \
            [e.upper() for e in ll[1].split(", ")] + \
            [e.upper() for e in ll[6].split(", ")] + \
            [e.upper() for e in ll[8].split(", ")] + \
            [e.upper() for e in ll[15].split(", ")] + \
            [e.upper() for e in ll[16].split(", ")] + \
            [e.upper() for e in ll[17].split(", ")] + \
            [e.upper() for e in ll[23].split(", ")] + \
            [e.upper() for e in ll[29].split(", ")] + \
            [e.upper() for e in ll[30].split(", ")] + \
            [e.upper() for e in ll[33].split(", ")] + \
            [e.upper() for e in ll[35].split(", ")] + \
            [e.upper() for e in ll[37].split(", ")]

  symbols = filter(None, symbols)
  if(not symbols): continue

  # Write
  outFile.write("\t".join([ens_id,official_symbol,"&".join(symbols)])+"\n")

# Termination
inFile.close()
outFile.close()


