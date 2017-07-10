# This script takes MGI annotation files and create an alias.txt file for the mouse genome

# Import
import os
import sys

# Input
inFileName1 = "./MGI_Gene_Model_Coord.rpt"
inFileName2 = "./MRK_List2.rpt"
outFileName = "./alias.txt"

# Creating MGI to ENSEMBL dictionary
convDict = dict()
inFile = open(inFileName1,"r")
inFile.readline()
for line in inFile:
  ll = line[:-1].split("\t")
  # MGI -> (ENSEMBL, [MGI, Entrez, VEGA])
  convDict[ll[0]] = (ll[10],[ll[0],ll[5],ll[15]])
inFile.close()

# Iterating over input file
inFile = open(inFileName2,"r")
outFile = open(outFileName,"w")
inFile.readline()
for line in inFile:

  ll = line[:-1].split("\t")

  # Ensembl ID
  try: ens_id = convDict[ll[0]][0]
  except Exception: continue
  if(not ens_id): continue
  if(ens_id == "null"): continue

  # Official Symbol
  official_symbol = ll[6]

  # Other IDs
  other_ids = convDict[ll[0]][1]
  
  # Symbols = Official Symbol, Synonyms, MGI, Entrez, VEGA 
  symbols = [e.upper() for e in ll[6].split("|")] + [e.upper() for e in ll[11].split("|")] + other_ids
  symbols = filter(None, symbols)
  symbols = [e for e in symbols if e != "null"]
  if(not symbols): continue

  # Write
  outFile.write("\t".join([ens_id,official_symbol,"&".join(symbols)])+"\n")

# Termination
inFile.close()
outFile.close()


