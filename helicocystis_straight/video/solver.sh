#!/bin/bash

#SBATCH --partition=long
#SBATCH --cpus-per-task=24
#SBATCH --mem=8G


apptainer run --bind ~/projects/nhm/jmcdermo/:/mnt --pwd /mnt/spirals/helicocystis_straight/video/base_case ~/apps/openfoam_12.sif bash -c "
decomposePar &&
mpirun --use-hwthread-cpus -n 24 --oversubscribe icoFoam -parallel | tee log.icoFoam"

