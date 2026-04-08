#!/bin/bash

#SBATCH --array=0
#SBATCH --partition=short
#SBATCH --cpus-per-task=24
#SBATCH --mem=8G



apptainer run --bind ~/projects/nhm/jmcdermo/:/mnt --pwd /mnt/spirals/stromatocystites/Re5000 ~/apps/openfoam_12.sif bash -c "
decomposePar &&
mpirun --use-hwthread-cpus -n 24 --oversubscribe icoFoam -parallel | tee log.icoFoam
foamLog log.icoFoam
"

# plot residuals and save inside each case file in postProcessing/
echo "plotting residuals..."
gnuplot residuals.gnu
