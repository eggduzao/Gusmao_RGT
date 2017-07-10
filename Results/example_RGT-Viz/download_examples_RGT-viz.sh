TARGETS="http://www.molcell.rwth-aachen.de/dc/data/cDC_WT_H3K4me3.bw
http://www.molcell.rwth-aachen.de/dc/data/cDC_WT_H3K27me3.bw
http://www.molcell.rwth-aachen.de/dc/data/cDC_WT_H3K4me1.bw
http://www.molcell.rwth-aachen.de/dc/data/cDC_PU1.bw
http://www.molcell.rwth-aachen.de/dc/data/CDP_WT_H3K4me3.bw
http://www.molcell.rwth-aachen.de/dc/data/CDP_WT_H3K27me3.bw
http://www.molcell.rwth-aachen.de/dc/data/CDP_WT_H3K4me1.bw
http://www.molcell.rwth-aachen.de/dc/data/CDP_PU1.bw"

for BW in $TARGETS; do
  FILE=$(basename $BW)
  NAME=${FILE%.*}
  wget $BW -O ./data/${FILE}
done

# other resources
#http://www.molcell.rwth-aachen.de/dc/data/MPP_WT_H3K4me3.bw
#http://www.molcell.rwth-aachen.de/dc/data/pDC_WT_H3K4me3.bw
#http://www.molcell.rwth-aachen.de/dc/data/MPP_WT_H3K27me3.bw
#http://www.molcell.rwth-aachen.de/dc/data/pDC_WT_H3K27me3.bw
#http://www.molcell.rwth-aachen.de/dc/data/MPP_WT_H3K4me1.bw
#http://www.molcell.rwth-aachen.de/dc/data/pDC_WT_H3K4me1.bw
#http://www.molcell.rwth-aachen.de/dc/data/MPP_PU1.bw
#http://www.molcell.rwth-aachen.de/dc/data/pDC_PU1.bw



