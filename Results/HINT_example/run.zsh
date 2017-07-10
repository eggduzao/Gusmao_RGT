#!/bin/zsh

# Open Parameters
hmm_file="--hmm-file=XXX"
bias_file="--bias-table=XXX"
organism="--organism=hg19"
estimate_bias_correction="--estimate-bias-correction"
default_bias_correction="--default-bias-correction"
default_bias_type="--default-bias-type=ATAC"
output_location="--output-location=./Output/"
print_raw_signal="--print-raw-signal=./Output/raw_signal.wig"
print_bc_signal="--print-bc-signal=./Output/bc-signal.wig"
print_norm_signal="--print-norm-signal=./Output/norm-signal.wig"
print_slope_signal="--print-slope-signal=./Output/slope-signal.wig"
dnase_bias_correction_k="--dnase-bias-correction-k=6"

# Hidden Parameters
rgt-hint $estimate_bias_correction $organism $dnase_bias_correction_k $output_location $print_raw_signal $print_bc_signal $print_norm_signal $print_slope_signal "./InputMatrix_HINT_DNase.txt"


