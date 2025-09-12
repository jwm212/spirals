#!/bin/bash

##### RUNNING THIS WILL DELETE ANY PREVIOUS DATA IN THESE CASES #####

#SBATCH --array=0-4
#SBATCH --partition=short
#SBATCH --cpus-per-task=1
#SBATCH --mem=6G

cases=(deg0 deg45 deg90 deg135 deg180)
apptainer run --bind ~/projects/nhm/jmcdermo/:/mnt --pwd /mnt/spirals/stromatocystites/orientation/${cases[$SLURM_ARRAY_TASK_ID]} ~/apps/openfoam_12.sif bash -c "
foamCleanTutorials &&
blockMesh &&
snappyHexMesh -overwrite | tee log.snappyHexMesh &&
checkMesh | tee log.checkMesh"
