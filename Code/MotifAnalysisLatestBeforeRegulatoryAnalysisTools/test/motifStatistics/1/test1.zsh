#!/bin/zsh

coord_file="/work/eg474423/eg474423_RegulatoryAnalysisTools/exp/motifanalysis/test/motifStatistics/1/coordinates/macs_peaks.bed"
motif_list="/work/eg474423/eg474423_RegulatoryAnalysisTools/exp/motifanalysis/test/motifStatistics/1/selectedFactors.bed"
gene_list="/work/eg474423/eg474423_RegulatoryAnalysisTools/exp/motifanalysis/test/motifStatistics/1/selectedGenes.bed"
assoc_coord_file="/work/eg474423/eg474423_RegulatoryAnalysisTools/exp/motifanalysis/test/motifStatistics/1/coord_association.bed"
mpbs_file="/work/eg474423/eg474423_RegulatoryAnalysisTools/exp/motifanalysis/test/motifStatistics/1/motifMatching/FACTOR1.bed,/work/eg474423/eg474423_RegulatoryAnalysisTools/exp/motifanalysis/test/motifStatistics/1/motifMatching/FACTOR2.bed,/work/eg474423/eg474423_RegulatoryAnalysisTools/exp/motifanalysis/test/motifStatistics/1/motifMatching/FACTOR3.bed"
mpbs_final_file="/work/eg474423/eg474423_RegulatoryAnalysisTools/exp/motifanalysis/test/motifStatistics/1/motifMatching/mpbs.bed"

genome_location="/work/eg474423/eg474423_RegulatoryAnalysisTools/exp/motifanalysis/test/motifStatistics/1/genome/"
association_file="/work/eg474423/eg474423_RegulatoryAnalysisTools/exp/motifanalysis/test/motifStatistics/1/geneAssocy.bed"
chrom_sizes_file="/work/eg474423/eg474423_RegulatoryAnalysisTools/exp/motifanalysis/test/motifStatistics/1/chromSizes.bed"
pwm_dataset="/work/eg474423/eg474423_RegulatoryAnalysisTools/exp/motifanalysis/test/motifStatistics/1/factors/"
logo_location="../factors/"
random_coordinates="/work/eg474423/eg474423_RegulatoryAnalysisTools/exp/motifanalysis/test/motifStatistics/1/rand.bed"

motif_match_fpr="0.0001"
motif_match_precision="10000"
motif_match_pseudocounts="0.1"
multiple_test_alpha="0.05"
promoter_length="6"
maximum_association_length="10"
cobinding="2"
cobinding_enriched_only="N"
enriched_pvalue="0.0886125824738"
rand_proportion_size="1.5"

output_location="/work/eg474423/eg474423_RegulatoryAnalysisTools/exp/motifanalysis/test/motifStatistics/1/out1/"
print_association="Y"
print_mpbs="Y"
print_results_text="Y"
print_results_html="Y"
print_enriched_genes="Y"
print_rand_coordinates="Y"
print_graph_mmscore="Y"
#print_graph_heatmap="Y"

motifStatistics "-coord_file="$coord_file "-motif_list="$motif_list "-gene_list="$gene_list  "-genome_location="$genome_location "-association_file="$association_file "-chrom_sizes_file="$chrom_sizes_file "-pwm_dataset="$pwm_dataset "-logo_location="$logo_location "-random_coordinates="$random_coordinates "-motif_match_fpr="$motif_match_fpr "-motif_match_precision="$motif_match_precision "-motif_match_pseudocounts="$motif_match_pseudocounts "-multiple_test_alpha="$multiple_test_alpha "-promoter_length="$promoter_length "-maximum_association_length="$maximum_association_length "-cobinding="$cobinding "-cobinding_enriched_only="$cobinding_enriched_only "-enriched_pvalue="$enriched_pvalue "-rand_proportion_size="$rand_proportion_size "-output_location="$output_location "-print_association="$print_association "-print_mpbs="$print_mpbs "-print_results_text="$print_results_text "-print_results_html="$print_results_html "-print_enriched_genes="$print_enriched_genes "-print_rand_coordinates="$print_rand_coordinates "-print_graph_mmscore="$print_graph_mmscore 
# "-assoc_coord_file="$assoc_coord_file
# "-mpbs_file="$mpbs_file
# "-mpbs_final_file="$mpbs_final_file
