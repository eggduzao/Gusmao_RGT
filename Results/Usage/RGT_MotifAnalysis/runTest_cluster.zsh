#!/bin/zsh

bsub -J "TEST" -o "TEST_out.txt" -e "TEST_err.txt" -W 40:00 -M 20000 -S 100 -P izkf -R "select[hpcwork]" ./runTest_pipeline.zsh


