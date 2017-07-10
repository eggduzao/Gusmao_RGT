#!/bin/zsh

# Setup RGT Genome

Before starting this analysis, we need to set up some additional datasets required by the motifanalysis tool.
First, we need to obtain the mouse genome sequence and the motif logo graphs, which can easily be done by performing the following steps:

1. Find your RGT Data folder.
2. From the RGT Data folder, type:

python setupGenomicData.py --mm9
python setupLogoData.py --jaspar-vertebrates --uniprobe-primary

More details on additional data setup, please check: configure genomic data and configure motif logos.

# Create results folder

We are going to store the results of this analysis in a new folder, to create the folder change the directory to this tutorial's example folder and type:

mkdir -p motif_analysis

# Perform motif matching

Finally, we are ready to perform the first step of the motif analysis, which consists of the motif matching. In this step we are going to find putative binding sites of a number of transcription factors into the genome of the mouse (mm9). To perform the motif match, still within this tutorial's example folder, type the following command:

rgt-motifanalysis --matching --organism mm9 --rand-proportion 3 --output-location motif_analysis motifanalysis_EM.txt

Let's check each part of the above command:

- rgt-motifanalysis --matching: This is the motif match command call. In order to know all the options you can use in the motif match analysis please type: 

rgt-motifanalysis --matching -h

- --organism mm9: Set the organism being analyzed to mm9.

- --rand-proportion 3: Since we plan to perform a motif enrichment after the matching, we also need putative binding sites at random regions. This command tells the tool to generate random putative binding sites with size three times larger than the input peak. In real scenarios this proportion should be set to 10 or more for statistical accuracy.

- --output-location motif_analysis: The putative binding sites (cDC_PU1_mpbs.bed), the set of random genomic regions (random_regions.bed) and the set of putative binding sites inside the random genomic regions (random_regions_mpbs.bed) will be written into this output location, under a folder named "Match".

-- motifanalysis_EM.txt: The only required argument represents the experimental matrix for this analysis. It contains the peak file which resulted from the previous tutorial section ("Implementing your own peak caller"). This experimental matrix is very simple since it contains only one input file. However, it might contain any number of input files (regions) and also genes to narrow the putative binding site search. For more information please refer to this manual.

# Perform motif enrichment

With the results of the motif matching, we can perform the motif enrichment. This analysis consists on veryfying which transcription factors are enriched in our input region (PU1 peaks of cell type cDC). To perform the motif enrichment type the following command:

rgt-motifanalysis --enrichment --organism mm9 --output-location motif_analysis motifanalysis_EM.txt motif_analysis

Let's check each part of the above command:

- rgt-motifanalysis --enrichment: This is the motif enrichment command call. In order to know all the options you can use in the motif enrichment analysis please type: 

rgt-motifanalysis --enrichment -h

- --organism mm9: Set the organism being analyzed to mm9.

--output-location motif_analysis: The results of the motif enrichment will be written into this folder. Check the next sub-section below for the description and interpretation of these results.

-- motifanalysis_EM.txt: The first required argument represents the experimental matrix containing the input files, as in the motif matching step.

-- motif_analysis: The second required argument represents the location in which we selected to output the motif matching results, which was the folder 'motif_analysis'.

# Describe results of motif enrichment

The motif enrichment tool outputs files inside the following folder structure: <output_folder>/<name_of_experimental_matrix>/<name_of_region>. In our example, the results will be inside: motif_analysis/motifanalysis_EM/cDC_PU1.

Let's explore the motif enrichment output:

- mpbs_ev.bed: Contains all the putative binding sites found inside PU1 peaks of cDC cell type.

- randtest_statistics.html and randtest_statistics.txt: Contains the results of the analyses in HTML and txt (tab-separated) format. The HTML table looks like this:

TABLE HTML

In this table we have information regarding the motif name, motif logo, enrichment p-value (uncorrected and multiple-test corrected), the statistics of the fisher test (A, B, C and D), the foreground enrichment frequency, background enrichment frequency and a link to perform a Gene Ontology search with the genes in which the putative transcription factors were associated to.

You can observe that PU1 motifs were ranked in the top (UP00085_1_Sfpi1_primary and MA0080.3.Spi1). Furthermore, we observed that other transcription factors were also enriched in these regions, such as ELF1, FLI1, Ets1, Erg, ELK4 and many others. These transcription factors are putative co-binding or regulatory partners of PU.1 and are connected with PU.1 in its regulatory network within the cDC cell type.

For more information on the motif analysis, please refer to the tool section in this website.


