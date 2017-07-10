#!/bin/zsh

bsub -J "MTEST" -o "MTEST_out.txt" -e "MTEST_err.txt" -W 100:00 -M 12000 -S 100 -P izkf -R "select[hpcwork]" ./motifMatching_pipeline.zsh


