#!/bin/bash

##### RUNNING THIS WILL DELETE ANY PREVIOUS DATA IN THESE CASES #####

#SBATCH --partition=short
#SBATCH --cpus-per-task=1
#SBATCH --mem=6G

apptainer run --bind ~/projects/nhm/jmcdermo/:/mnt --pwd /mnt/spirals/helicocystis/base_case ~/apps/openfoam_12.sif bash -c "
foamCleanTutorials &&
blockMesh &&
snappyHexMesh -overwrite | tee log.snappyHexMesh &&
checkMesh | tee log.checkMesh &&
foamToVTK -faceSet wrongFaces -time 0"
