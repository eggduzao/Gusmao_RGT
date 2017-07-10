#!/bin/zsh

# Import
#export PATH=/home/egg/Projects/RGT/Tests/MotifAnalysisOld/Installation/bin/:$PATH
#export PYTHONPATH=/home/egg/Projects/RGT/Tests/MotifAnalysisOld/Installation/lib/python2.6/site-packages/:$PYTHONPATH

coord_file="-coord_file=/home/egg/Projects/RGT/Tests/MotifAnalysisOld/Execution/Input/cdp_gain_final.bed"
motif_list="-motif_list=/home/egg/Projects/RGT/Tests/MotifAnalysisOld/Execution/Input/motif_list.txt"
#gene_list="-gene_list="
#assoc_coord_file="-assoc_coord_file="
#mpbs_file="-mpbs_file="
#mpbs_final_file="-mpbs_final_file="

#genome_list="-genome_list="
#association_file="-association_file="
#chrom_sizes_file="-chrom_sizes_file=/home/egg/Projects/RGT/Tests/MotifAnalysisOld/Execution/Input/chrom.sizes"
#pwm_dataset="-pwm_dataset="
#logo_location="-logo_location="
#random_coordinates="-random_coordinates="

organism="-organism=hg19"
#motif_match_fpr="-motif_match_fpr="
#motif_match_precision="-motif_match_precision="
#motif_match_pseudocounts="-motif_match_pseudocounts="
#multiple_test_alpha="-multiple_test_alpha="
#promoter_length="-promoter_length="
#maximum_association_length="-maximum_association_length="
#cobinding="-cobinding="
#cobinding_enriched_only="-cobinding_enriched_only="
#enriched_pvalue="-enriched_pvalue="
rand_proportion_size="-rand_proportion_size=1.0"
all_coord_evidence="-all_coord_evidence=Y"

output_location="-output_location=/home/egg/Projects/RGT/Tests/MotifAnalysisOld/Execution/Results/"
#print_association="-print_association="
#print_mpbs="-print_mpbs="
#print_results_text="-print_results_text="
#print_results_html="-print_results_html="
#print_enriched_genes="-print_enriched_genes="
#print_rand_coordinates="-print_rand_coordinates="
#print_graph_mmscore="-print_graph_mmscore="
#print_graph_heatmap="-print_graph_heatmap="

rgt-motifanalysis enrichment $coord_file $motif_list $organism $rand_proportion_size $all_coord_evidence $output_location


