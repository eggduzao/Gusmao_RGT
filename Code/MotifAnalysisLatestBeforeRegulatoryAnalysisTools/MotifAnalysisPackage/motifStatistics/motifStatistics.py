#################################################################################################
# Performs fisher exact test with multiple testing correction on MPBSs found on specific
# coordinates, concerning the enrichment for a specific set of genes.
#################################################################################################

# Libraries
import os
import sys
import util
import sort
import html
import motif
import graphs
import genome
import constants
import statistics
import bedFunctions

def main():

    #################################################################################################
    ##### PARAMETERS ################################################################################
    #################################################################################################

    # Parameters
    params = []

    params.append("\nMotifStatistics -- Version 0.0.1")
    params.append("Performs fisher exact test with multiple testing correction on motif predicted")
    params.append("binding sites. For full documentation visit the following webpage:")
    params.append("www.followingwebpage.com")

    params.append("\nRequired Input: ")
    params.append("  -coord_file=<FILE>        Coordinate file containing the regions of the genome")
    params.append("                            where the motif matching will be performed. If")
    params.append("                            None, -assoc_coord_file option must be used.")
    params.append("                            Format: bed.")
    params.append("                            Default: None.")
    params.append("  -motif_list=<FILE>        Motif list file containing the factors that will be")
    params.append("                            tested, split by line break. If None, uses entire")
    params.append("                            dataset defined in -pwm_dataset.")
    params.append("                            Format: plain text.")
    params.append("                            Default: None.")
    params.append("  -gene_list=<FILE>         Gene list file containing the genes that will")
    params.append("                            consist the enriched set. If None, considers entire")
    params.append("                            coordinate file as enriched.")
    params.append("                            Format: plain text.")
    params.append("                            Default: None.")
    params.append("  -assoc_coord_file=<FILE>  Coordinate file already annotated with the enriched")
    params.append("                            genes. Check full documentation for annotation")
    params.append("                            format. If None, uses -coord_file, -gene_list and")
    params.append("                            -association_file options to generate coordinate-")
    params.append("                            gene association. Otherwise, ignores -coord_file and")
    params.append("                            -gene_list options.")
    params.append("                            Format: bed.")
    params.append("                            Default: None.")
    params.append("  -mpbs_file=<FILE1[,FILE2,...,FILEN]>")
    params.append("                            Motif matching files containing the motif predicted")
    params.append("                            binding sites. The name of the file is considered as")
    params.append("                            the name of the factor. If None, uses -motif_list")
    params.append("                            and -pwm_dataset options or -mpbs_final_file option.")
    params.append("                            Otherwise, ignores -motif_list option.")
    params.append("                            Format: bed.")
    params.append("                            Default: None.")
    params.append("  -mpbs_final_file=<FILE>   Motif matching file containing the motif predicted")
    params.append("                            binding sites in the correct format for it to be")
    params.append("                            separated in evidence / non-evidence and randomic")
    params.append("                            sets. Check full documentation for more information.")
    params.append("                            Format: bed.")
    params.append("                            Default: None.")

    params.append("\nOptional Input: ")
    params.append("  -genome_location=<PATH>   Location of the genome. It must contain one fasta")
    params.append("                            file for each chromosome (on standard nomenclature).")
    params.append("                            Format: fasta.")
    params.append("                            Default: Use version in server (mm9).")
    params.append("  -association_file=<FILE>  File containing the location of all genes. The")
    params.append("                            gene name must be the same as the ones in gene_list")
    params.append("                            option. Check full documentation for more details on")
    params.append("                            format.")
    params.append("                            Format: bed.")
    params.append("                            Default: Use version in server (genes in refseq).")
    params.append("  -chrom_sizes_file=<FILE>  File containing the total length of each chromosome.")
    params.append("                            It is a plain text file containing the chromosome")
    params.append("                            name and the length in each line, separated by tab.")
    params.append("                            Format: plain text.")
    params.append("                            Default: Use version in server (mm9).")
    params.append("  -pwm_dataset=<PATH>       Path containing PWM files in jaspar format. Each")
    params.append("                            file name is considered as the factor name.")
    params.append("                            Format: jaspar.")
    params.append("                            Default: Use version in server.")
    params.append("  -logo_location=<PATH>     Path that contains png images representing motif")
    params.append("                            logos. Each file must contain the same name of the")
    params.append("                            respective factor inside -pwm_dataset.")
    params.append("                            Format: png.")
    params.append("                            Default: Use version in server.")
    params.append("  -random_coordinates=<FILE>")
    params.append("                            File containing the random coordinates for fisher")
    params.append("                            test. If None, create random coordinates. The number")
    params.append("                            of coordinates equals the size of the input")
    params.append("                            coordinates file x -rand_proportion_size.")
    params.append("                            Format: png.")
    params.append("                            Default: None.")

    params.append("\nInput Parameters: ")
    params.append("  -motif_match_fpr=<FLOAT>  False positive rate cutoff for motif matching.")
    params.append("                            Default: 0.0001.")
    params.append("  -motif_match_precision=<INT>")
    params.append("                            Score distribution precision for motif matching.")
    params.append("                            Default: 10000.")
    params.append("  -motif_match_pseudocounts=<FLOAT>")
    params.append("                            Pseudocounts to be added to raw counts of each PWM.")
    params.append("                            Default: 0.1.")
    params.append("  -multiple_test_alpha=<FLOAT>")
    params.append("                            Alpha value for multiple test.")
    params.append("                            Default: 0.05.")
    params.append("  -promoter_length=<INT>    Length of the promoter region (in bp) considered on")
    params.append("                            the creation of the coordinate-gene association.")
    params.append("                            Default: 1000.")
    params.append("  -maximum_association_length=<INT>")
    params.append("                            Maximum distance between a coordinate and a gene")
    params.append("                            (in bp) in order for the former to be considered")
    params.append("                            associated with the latter.")
    params.append("                            Default: 50000.")
    params.append("  -cobinding=<INT1[,INT2,...,INTN]>")
    params.append("                            Number of cobinding combinations to test.")
    params.append("                            Default: None.")
    params.append("  -cobinding_enriched_only=<Y|N>")
    params.append("                            If Y then only enriched factors are tested for")
    params.append("                            cobinding. If N, all factors are tested.")
    params.append("                            Default: Y.")
    params.append("  -enriched_pvalue=<FLOAT>  P-value cutoff to consider a factor, or factor")
    params.append("                            combination as enriched or not enriched.")
    params.append("                            Default: 0.05.")
    params.append("  -rand_proportion_size=<FLOAT>")
    params.append("                            If random coordinates need to be created, then it")
    params.append("                            will be created a number of coordinates that equals")
    params.append("                            this parameter x the number of input coordinates.")
    params.append("                            Default: 1.0.")

    params.append("\nOutput Options: ")
    params.append("  -output_location=<PATH>   Path where the output files will be written.")
    params.append("                            Default: current directory.")
    params.append("  -print_association=<Y|N>  Whether to output a bigbed file containing the")
    params.append("                            coordinate-gene association + MPBSs that occured")
    params.append("                            inside all coordinates.")
    params.append("                            Default: Y.")
    params.append("  -print_mpbs=<Y|N>         Whether to output a bigbed file containing all MPBSs")
    params.append("                            found on input and random coordinates.")
    params.append("                            Default: Y.")
    params.append("  -print_results_text=<Y|N> Whether to output the fisher test results in text")
    params.append("                            format.")
    params.append("                            Default: Y.")
    params.append("  -print_results_html=<Y|N> Whether to output the fisher test results in html")
    params.append("                            format.")
    params.append("                            Default: Y.")
    params.append("  -print_enriched_genes=<Y|N>")
    params.append("                            Whether to output multiple files for each factor (or")
    params.append("                            combination of factors) containing a list of")
    params.append("                            enriched genes where a MPBS for that factor (or")
    params.append("                            combination of factors) occured.")
    params.append("                            Default: Y.")
    params.append("  -print_rand_coordinates=<Y|N>")
    params.append("                            Whether to output a bigbed file containing the")
    params.append("                            random coordinates.")
    params.append("                            Default: Y.")
    params.append("  -print_graph_mmscore=<Y|N>")
    params.append("                            Whether to output graphs containing the motif")
    params.append("                            matching score distribution for the MPBSs found on")
    params.append("                            the input and random coordinates.")
    params.append("                            Default: N.")
    params.append("  -print_graph_heatmap=<Y|N>")
    params.append("                            Whether to output graphs containing heatmaps")
    params.append("                            created based on the corrected p-values of the")
    params.append("                            multiple testing.")
    params.append("                            Default: N.")
    params.append("")
    if(len(sys.argv) <= 1):
        for e in params: print e
        sys.exit(0)

    #################################################################################################
    ##### INPUT #####################################################################################
    #################################################################################################

    # Input parameters dictionary
    inputParameters = util.readInputParameters(sys.argv[1:])

    # Required Input
    flagC = False; flagM = False; flagG = False; flagCG = False; flagMM = False; flagMF = False
    if("-coord_file" in inputParameters.keys()): flagC = True
    else: inputParameters["-coord_file"] = None
    if("-motif_list" in inputParameters.keys()): flagM = True
    else: inputParameters["-motif_list"] = None
    if("-gene_list" in inputParameters.keys()): flagG = True
    else: inputParameters["-gene_list"] = None
    if("-assoc_coord_file" in inputParameters.keys()): flagCG = True
    else: inputParameters["-assoc_coord_file"] = None
    if("-mpbs_file" in inputParameters.keys()):
        flagMM = True
        inputParameters["-mpbs_file"] = inputParameters["-mpbs_file"].split(",")
    else: inputParameters["-mpbs_file"] = None
    if("-mpbs_final_file" in inputParameters.keys()): flagMF = True
    else: inputParameters["-mpbs_final_file"] = None

    # Required input verification
    if(not flagC and not flagCG): 
        print "ERROR: You must specify a coordinate file where the motif matching\n       will be performed using -coord_file or -assoc_coord_file."
        sys.exit(0)

    # Optional Input
    flagR = False
    if("-genome_location" in inputParameters.keys()):
        if(inputParameters["-genome_location"][-1] != "/"): inputParameters["-genome_location"] += "/"
    else: inputParameters["-genome_location"] = "/work/eg474423/ig440396_dendriticcells/local/mm9/"
    if("-association_file" in inputParameters.keys()): pass
    else: inputParameters["-association_file"] = "/work/eg474423/ig440396_dendriticcells/data/annotation/mm9_ref_name_corrected.bed"
    if("-chrom_sizes_file" in inputParameters.keys()): pass
    else: inputParameters["-chrom_sizes_file"] = "/work/eg474423/ig440396_dendriticcells/data/annotation/mm9.size"
    if("-pwm_dataset" in inputParameters.keys()):
        if(inputParameters["-pwm_dataset"][-1] != "/"): inputParameters["-pwm_dataset"] += "/"
    else: inputParameters["-pwm_dataset"] = "/work/eg474423/ig440396_dendriticcells/data/motifs/jasparformat/"
    if("-logo_location" in inputParameters.keys()):
        if(inputParameters["-logo_location"][-1] != "/"): inputParameters["-logo_location"] += "/"
    else: inputParameters["-logo_location"] = "../../logos/"
    if("-random_coordinates" in inputParameters.keys()): flagR = True
    else: inputParameters["-random_coordinates"] = None

    # Input Parameters
    if("-motif_match_fpr" in inputParameters.keys()): inputParameters["-motif_match_fpr"] = float(inputParameters["-motif_match_fpr"])
    else: inputParameters["-motif_match_fpr"] = 0.0001
    if("-motif_match_precision" in inputParameters.keys()): inputParameters["-motif_match_precision"] = int(inputParameters["-motif_match_precision"])
    else: inputParameters["-motif_match_precision"] = 10**4
    if("-motif_match_pseudocounts" in inputParameters.keys()): inputParameters["-motif_match_pseudocounts"] = float(inputParameters["-motif_match_pseudocounts"])
    else: inputParameters["-motif_match_pseudocounts"] = 0.1
    if("-multiple_test_alpha" in inputParameters.keys()): inputParameters["-multiple_test_alpha"] = float(inputParameters["-multiple_test_alpha"])
    else: inputParameters["-multiple_test_alpha"] = 0.05
    if("-promoter_length" in inputParameters.keys()): inputParameters["-promoter_length"] = int(inputParameters["-promoter_length"])
    else: inputParameters["-promoter_length"] = 1000
    if("-maximum_association_length" in inputParameters.keys()): inputParameters["-maximum_association_length"] = int(inputParameters["-maximum_association_length"])
    else: inputParameters["-maximum_association_length"] = 50000
    if("-cobinding" in inputParameters.keys()): 
        inputParameters["-cobinding"] = list(set([1]+[int(e) for e in inputParameters["-cobinding"].split(",")]))
        inputParameters["-cobinding"].sort()
    else: inputParameters["-cobinding"] = [1]
    if("-cobinding_enriched_only" in inputParameters.keys()):
        if(inputParameters["-cobinding_enriched_only"] == "Y"): inputParameters["-cobinding_enriched_only"] = True
        else: inputParameters["-cobinding_enriched_only"] = False
    else: inputParameters["-cobinding_enriched_only"] = True
    if("-enriched_pvalue" in inputParameters.keys()): inputParameters["-enriched_pvalue"] = float(inputParameters["-enriched_pvalue"])
    else: inputParameters["-enriched_pvalue"] = 0.05
    if("-rand_proportion_size" in inputParameters.keys()): inputParameters["-rand_proportion_size"] = float(inputParameters["-rand_proportion_size"])
    else: inputParameters["-rand_proportion_size"] = 1.0

    # Output Options
    if("-output_location" in inputParameters.keys()):
        if(inputParameters["-output_location"][-1] != "/"): inputParameters["-output_location"] += "/"
    else: inputParameters["-output_location"] = "./"
    if("-print_association" in inputParameters.keys()):
        if(inputParameters["-print_association"] == "Y"): inputParameters["-print_association"] = True
        else: inputParameters["-print_association"] = False
    else: inputParameters["-print_association"] = True
    if("-print_mpbs" in inputParameters.keys()):
        if(inputParameters["-print_mpbs"] == "Y"): inputParameters["-print_mpbs"] = True
        else: inputParameters["-print_mpbs"] = False
    else: inputParameters["-print_mpbs"] = True
    if("-print_results_text" in inputParameters.keys()):
        if(inputParameters["-print_results_text"] == "Y"): inputParameters["-print_results_text"] = True
        else: inputParameters["-print_results_text"] = False
    else: inputParameters["-print_results_text"] = True
    if("-print_results_html" in inputParameters.keys()):
        if(inputParameters["-print_results_html"] == "Y"): inputParameters["-print_results_html"] = True
        else: inputParameters["-print_results_html"] = False
    else: inputParameters["-print_results_html"] = True
    if("-print_enriched_genes" in inputParameters.keys()):
        if(inputParameters["-print_enriched_genes"] == "Y"): inputParameters["-print_enriched_genes"] = True
        else: inputParameters["-print_enriched_genes"] = False
    else: inputParameters["-print_enriched_genes"] = True
    if("-print_rand_coordinates" in inputParameters.keys()):
        if(inputParameters["-print_rand_coordinates"] == "Y"): inputParameters["-print_rand_coordinates"] = True
        else: inputParameters["-print_rand_coordinates"] = False
    else: inputParameters["-print_rand_coordinates"] = True
    if("-print_graph_mmscore" in inputParameters.keys()):
        if(inputParameters["-print_graph_mmscore"] == "Y"): inputParameters["-print_graph_mmscore"] = True
        else: inputParameters["-print_graph_mmscore"] = False
    else: inputParameters["-print_graph_mmscore"] = False
    if("-print_graph_heatmap" in inputParameters.keys()):
        if(inputParameters["-print_graph_heatmap"] == "Y"): inputParameters["-print_graph_heatmap"] = True
        else: inputParameters["-print_graph_heatmap"] = False
    else: inputParameters["-print_graph_heatmap"] = False

    #################################################################################################
    ##### COORDINATE-GENE ASSOCIATION ###############################################################
    #################################################################################################
    
    if(not flagCG): # If coordinate-gene association was not given, create the association with coordinate and gene files.

        # Reading and sorting coordinate file
        coordDict = bedFunctions.createBedDictFromSingleFile(inputParameters["-coord_file"], separator="\t")
        coordDict = sort.sortBedDictionary(coordDict, field=0)
        
        if(not flagG): # If gene file was not given, consider all genes as evidence.
            coordDict, coordDictToPrint = genome.geneAssociationByPromoter(coordDict,None,inputParameters["-association_file"],inputParameters["-chrom_sizes_file"],inputParameters["-promoter_length"],inputParameters["-maximum_association_length"])
            evDict, nonEvDict = bedFunctions.separateEvidence(coordDict)
            evDictToPrint, nonEvDictToPrint = bedFunctions.separateEvidence(coordDictToPrint)

        else: # If gene file was given, create ev and nev sets.
            geneList = util.readList(inputParameters["-gene_list"]) # Reading gene list
            coordDict, coordDictToPrint = genome.geneAssociationByPromoter(coordDict,geneList,inputParameters["-association_file"],inputParameters["-chrom_sizes_file"],inputParameters["-promoter_length"],inputParameters["-maximum_association_length"])
            evDict, nonEvDict = bedFunctions.separateEvidence(coordDict)
            evDictToPrint, nonEvDictToPrint = bedFunctions.separateEvidence(coordDictToPrint)

    else: # If coordinate-gene association was given, read it.

        # Reading and sorting coordinate file
        coordDictToPrint = bedFunctions.createBedDictFromSingleFile(inputParameters["-assoc_coord_file"], separator="\t")
        coordDictToPrint = sort.sortBedDictionary(coordDictToPrint, field=0)
        coordDict = genome.removeProximityInformation(coordDictToPrint)

        # Separating evidence
        evDict, nonEvDict = bedFunctions.separateEvidence(coordDict)
        evDictToPrint, nonEvDictToPrint = bedFunctions.separateEvidence(coordDictToPrint)

    #################################################################################################
    ##### RANDOM COORDINATES ########################################################################
    #################################################################################################

    if(not flagR): # If random coordinates were not given, create it from scratch.
        randDict = bedFunctions.createRandomCoordinates(coordDict,inputParameters["-chrom_sizes_file"],prop=inputParameters["-rand_proportion_size"])
        randDict = sort.sortBedDictionary(randDict, field=0)

    else: # If random coordinates were given, read it.
        randDict = bedFunctions.createBedDictFromSingleFile(inputParameters["-random_coordinates"], separator="\t")
        randDict = sort.sortBedDictionary(randDict, field=0)

    #################################################################################################
    ##### MOTIF MATCHING ############################################################################
    #################################################################################################

    if(not flagMM and not flagMF): # If motif matching multiple factor files and final file were not given, perform motif matching.
        if(flagM): motifList = util.readList(inputParameters["-motif_list"])
        else:
            motifList = []
            for pwmFileName in os.listdir(inputParameters["-pwm_dataset"]):
                if(pwmFileName[-4:] == ".pwm"): motifList.append(pwmFileName[:-4])
        mpbsDictEv, statDictEv, geneDictEv = motif.motifMatchingBiopython(inputParameters["-cobinding"],motifList,evDict,inputParameters["-pwm_dataset"],inputParameters["-genome_location"],inputParameters["-output_location"],inputParameters["-motif_match_fpr"],inputParameters["-motif_match_pseudocounts"],inputParameters["-motif_match_precision"],"green")
        mpbsDictNev, statDictNev, geneDictNev = motif.motifMatchingBiopython(inputParameters["-cobinding"],motifList,nonEvDict,inputParameters["-pwm_dataset"],inputParameters["-genome_location"],inputParameters["-output_location"],inputParameters["-motif_match_fpr"],inputParameters["-motif_match_pseudocounts"],inputParameters["-motif_match_precision"],"red")
        mpbsDictRand, statDictRand, geneDictRand = motif.motifMatchingBiopython(inputParameters["-cobinding"],motifList,randDict,inputParameters["-pwm_dataset"],inputParameters["-genome_location"],inputParameters["-output_location"],inputParameters["-motif_match_fpr"],inputParameters["-motif_match_pseudocounts"],inputParameters["-motif_match_precision"],"black")

    elif(flagMF): # If motif matching final file was given, read it and create the motif counts to be used in fisher test.
        if(flagM): motifList = util.readList(inputParameters["-motif_list"])
        else:
            motifList = []
            motifFinalFile = open(inputParameters["-mpbs_final_file"],"r")
            for line in motifFinalFile:
                ll = line.strip().split("\t")
                if(ll[3] not in motifList): motifList.append(ll[3])
            motifFinalFile.close()
        mpbsDictEv, statDictEv, geneDictEv = motif.readMotifMatching(inputParameters["-cobinding"],evDict,inputParameters["-mpbs_final_file"],"green",motifList)
        mpbsDictNev, statDictNev, geneDictNev = motif.readMotifMatching(inputParameters["-cobinding"],nonEvDict,inputParameters["-mpbs_final_file"],"red",motifList)
        mpbsDictRand, statDictRand, geneDictRand = motif.readMotifMatching(inputParameters["-cobinding"],randDict,inputParameters["-mpbs_final_file"],"black",motifList)

    else: # If motif matching multiple factor files were given, read them and create the motif counts to be used in fisher test.
        mpbsDictEv, statDictEv, geneDictEv = motif.readMotifMatching(inputParameters["-cobinding"],evDict,inputParameters["-mpbs_file"],"green")
        mpbsDictNev, statDictNev, geneDictNev = motif.readMotifMatching(inputParameters["-cobinding"],nonEvDict,inputParameters["-mpbs_file"],"red")
        mpbsDictRand, statDictRand, geneDictRand = motif.readMotifMatching(inputParameters["-cobinding"],randDict,inputParameters["-mpbs_file"],"black")

    #################################################################################################
    ##### STATISTICS ################################################################################
    #################################################################################################

    # Evaluating statistics
    resultTableListNev = statistics.fisherMultiple(inputParameters["-enriched_pvalue"],inputParameters["-cobinding"],inputParameters["-multiple_test_alpha"],statDictEv,statDictNev,geneDictEv,inputParameters["-cobinding_enriched_only"])
    resultTableListRand = statistics.fisherMultiple(inputParameters["-enriched_pvalue"],inputParameters["-cobinding"],inputParameters["-multiple_test_alpha"],statDictEv,statDictRand,geneDictEv,inputParameters["-cobinding_enriched_only"])

    #################################################################################################
    ##### PRINTING OUTPUT ###########################################################################
    #################################################################################################

    # Print coordinate association + MPBSs (ev and nev)
    if(inputParameters["-print_association"]):

        outputFile = open(inputParameters["-output_location"]+"coord_association_temp.bed","w") # Output file

        # Print evDictToPrint
        for chrName in constants.getChromList(reference=[evDictToPrint]):
            for e in evDictToPrint[chrName]: 
                newGeneNames = []
                for g in e[2].split(":"):
                    if(len(g) < 2): newGeneNames.append(".")
                    elif(g[0] == "."): newGeneNames.append(g[1:])
                    else: newGeneNames.append(g)
                e[2] = ":".join(newGeneNames)                
                outputFile.write("\t".join([chrName]+[str(k) for k in e]+[str(e[0]),str(e[1]),"0,130,0"])+"\n")

        # Print nonEvDictToPrint
        for chrName in constants.getChromList(reference=[nonEvDictToPrint]):
            for e in nonEvDictToPrint[chrName]: 
                newGeneNames = []
                for g in e[2].split(":"):
                    if(len(g) < 2): newGeneNames.append(".")
                    elif(g[0] == "."): newGeneNames.append(g[1:])
                    else: newGeneNames.append(g)
                e[2] = ":".join(newGeneNames)                
                outputFile.write("\t".join([chrName]+[str(k) for k in e]+[str(e[0]),str(e[1]),"130,0,0"])+"\n")

        # Print mpbsDictEv
        for k in mpbsDictEv.keys():
            for e in mpbsDictEv[k].keys(): 
                for v in mpbsDictEv[k][e]: outputFile.write("\t".join([e]+[str(t) for t in v])+"\n")

        # Print mpbsDictNev
        for k in mpbsDictNev.keys():
            for e in mpbsDictNev[k].keys(): 
                for v in mpbsDictNev[k][e]: outputFile.write("\t".join([e]+[str(t) for t in v])+"\n")
        
        # Converting to bigbed
        outputFile.close()
        os.system("sort -k1,1 -k2,2n "+inputParameters["-output_location"]+"coord_association_temp.bed > "+inputParameters["-output_location"]+"coord_association.bed")
        bedFunctions.bedToBigBed(inputParameters["-output_location"]+"coord_association.bed",inputParameters["-chrom_sizes_file"],inputParameters["-output_location"]+"coord_association.bb",removeBed=True)
        os.system("rm "+inputParameters["-output_location"]+"coord_association_temp.bed")

    # Print all MPBSs
    if(inputParameters["-print_mpbs"]):

        outputFile = open(inputParameters["-output_location"]+"mpbs_temp.bed","w") # Output file

        # Print mpbsDictEv
        for k in mpbsDictEv.keys():
            for e in mpbsDictEv[k].keys(): 
                for v in mpbsDictEv[k][e]: outputFile.write("\t".join([e]+[str(t) for t in v])+"\n")

        # Print mpbsDictNev
        for k in mpbsDictNev.keys():
            for e in mpbsDictNev[k].keys(): 
                for v in mpbsDictNev[k][e]: outputFile.write("\t".join([e]+[str(t) for t in v])+"\n")

        # Print mpbsDictRand
        for k in mpbsDictRand.keys():
            for e in mpbsDictRand[k].keys(): 
                for v in mpbsDictRand[k][e]: outputFile.write("\t".join([e]+[str(t) for t in v])+"\n")
        
        # Converting to bigbed
        outputFile.close()
        os.system("sort -k1,1 -k2,2n "+inputParameters["-output_location"]+"mpbs_temp.bed > "+inputParameters["-output_location"]+"mpbs.bed")
        bedFunctions.bedToBigBed(inputParameters["-output_location"]+"mpbs.bed",inputParameters["-chrom_sizes_file"],inputParameters["-output_location"]+"mpbs.bb",removeBed=True)
        os.system("rm "+inputParameters["-output_location"]+"mpbs_temp.bed")

    # Print results as plain text files
    if(inputParameters["-print_results_text"]):

        # Iterating on cobinding combinations
        counter = 0
        for comb in inputParameters["-cobinding"]:

            # Creating header
            headerList = []
            for e in range(1,comb+1): headerList.append("FACTOR"+str(e))
            for e in ["P-VALUE","CORR.P-VALUE","A","B","C","D","PERCENT","BACK.PER.","GENES"]: headerList.append(e)

            # Printing nev statistics
            outputFile = open(inputParameters["-output_location"]+"nev_"+str(comb)+"_statistics.txt","w")
            outputFile.write("\t".join(headerList)+"\n")
            for e in resultTableListNev[counter]:
                outputFile.write("\t".join([str(k) for k in e[:-1]]))
                outputFile.write("\t"+",".join(e[-1])+"\n")
            outputFile.close()

            # Printing rand statistics
            outputFile = open(inputParameters["-output_location"]+"rand_"+str(comb)+"_statistics.txt","w")
            outputFile.write("\t".join(headerList)+"\n")
            for e in resultTableListRand[counter]:
                outputFile.write("\t".join([str(k) for k in e[:-1]]))
                outputFile.write("\t"+",".join(e[-1])+"\n")
            outputFile.close()

            counter += 1

    # Print results as html files
    if(inputParameters["-print_results_html"]):

        # Iterating on cobinding combinations
        counter = 0
        for comb in inputParameters["-cobinding"]:

            # Creating header
            headerList = []
            for e in range(1,comb+1): headerList.append("FACTOR"+str(e))
            for e in ["P-VALUE","CORR.P-VALUE","A","B","C","D","PERCENT","BACK.PER.","GENES"]: headerList.append(e)
            for e in range(0,comb): headerList.insert((e*2)+1,"MOTIF"+str(e+1))

            # Printing nev statistics
            html.printHTML(range(0,comb),len(headerList)-comb-1,headerList,inputParameters["-logo_location"],resultTableListNev[counter],inputParameters["-output_location"]+"nev_"+str(comb)+"_statistics.html")
            
            # Printing rand statistics
            html.printHTML(range(0,comb),len(headerList)-comb-1,headerList,inputParameters["-logo_location"],resultTableListRand[counter],inputParameters["-output_location"]+"rand_"+str(comb)+"_statistics.html")
            
            counter += 1

    # Print enriched genes on multiple files for each factor or combination of factors
    if(inputParameters["-print_enriched_genes"]):

        # Reading reference gene list if it is available
        if(flagG): geneListReference = util.readList(inputParameters["-gene_list"])
        else: geneListReference = None

        # Iterating on cobinding combinations
        counter = 0
        for comb in inputParameters["-cobinding"]:

            # Writing non-evidence genes
            outputFolderName = inputParameters["-output_location"]+"genesNev/"
            os.system("mkdir -p "+outputFolderName)
            for vec in resultTableListNev[counter]:
                outputFile = open(outputFolderName+"_".join([vec[e] for e in range(0,comb)])+".txt","w")
                if(geneListReference): outputFile.write("\n".join(sort.sortListByReference(vec[-1],geneListReference)))
                else: outputFile.write("\n".join(vec[-1]))
                outputFile.close()

            # Writing random genes
            outputFolderName = inputParameters["-output_location"]+"genesRand/"
            os.system("mkdir -p "+outputFolderName)
            for vec in resultTableListRand[counter]:
                outputFile = open(outputFolderName+"_".join([vec[e] for e in range(0,comb)])+".txt","w")
                if(geneListReference): outputFile.write("\n".join(sort.sortListByReference(vec[-1],geneListReference)))
                else: outputFile.write("\n".join(vec[-1]))
                outputFile.close()

            counter += 1

    # Print random coordinates
    if(inputParameters["-print_rand_coordinates"]):

        bedFunctions.printBedDict(randDict, inputParameters["-chrom_sizes_file"], inputParameters["-output_location"]+"rand.bb", out="bb", separator="\t")

    #################################################################################################
    ##### GRAPHS ####################################################################################
    #################################################################################################

    # Motif predicted binding sites score distribution
    if(inputParameters["-print_graph_mmscore"]):

        os.system("mkdir -p "+inputParameters["-output_location"]+"MM_score_distribution/")
        graphs.mpbsScoreHistogram([mpbsDictRand,mpbsDictNev,mpbsDictEv],["black","red","green"],[0.5,0.6,0.7],["rand","nev","ev"],inputParameters["-output_location"]+"MM_score_distribution/",bins=100,outExt="png")


    # TODO P-value heatmap
    if(inputParameters["-print_graph_heatmap"]): pass


#################################################################################################
##### MAIN ######################################################################################
#################################################################################################

if __name__ == '__main__':
    main()


