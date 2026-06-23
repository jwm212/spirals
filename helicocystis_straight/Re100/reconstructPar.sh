#!/bin/bash

#SBATCH --array=0
#SBATCH --partition=medium
#SBATCH --cpus-per-task=1
#SBATCH --mem=8G



apptainer run --bind ~/projects/nhm/jmcdermo/:/mnt --pwd /mnt/spirals/helicocystis_straight/Re100 ~/apps/openfoam_12.sif bash -c "
reconstructPar
"

rm -rf processor*