#!/bin/bash

#SBATCH --array=0
#SBATCH --partition=short
#SBATCH --cpus-per-task=1
#SBATCH --mem=8G



apptainer run --bind ~/projects/nhm/jmcdermo/:/mnt --pwd /mnt/spirals/stromatocystites/Re5000 ~/apps/openfoam_12.sif bash -c "
reconstructPar
"

# Remove processor dirs:
rm -rf ./processor*