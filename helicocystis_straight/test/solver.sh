#!/bin/bash

#SBATCH --partition=short
#SBATCH --cpus-per-task=24
#SBATCH --mem=6G

apptainer run --bind ~/projects/nhm/jmcdermo/:/mnt --pwd /mnt/spirals/helicocystis_straight/test/ ~/apps/openfoam_12.sif bash -c "
decomposePar &&
mpirun --use-hwthread-cpus -n 24 --oversubscribe icoFoam -parallel | tee log.icoFoam &&
reconstructPar &&
postProcess -func vorticity &&
foamLog log.icoFoam &&
foamToVTK"

