#!/bin/bash
#SBATCH --array=0-4
#SBATCH --job-name=h_st_Re10000
#SBATCH --partition=medium
#SBATCH --cpus-per-task=1
#SBATCH --mem=8G

times=(0:0.05 0.06:0.11 0.12:0.17 0.18:0.23 0.24:0.27)

cd $SCRATCH/$SLURM_JOB_NAME

apptainer run --bind $SCRATCH:/mnt --pwd $SCRATCH/$SLURM_JOB_NAME ~/apps/openfoam_12.sif bash -c "
reconstructPar -time '${times[$SLURM_ARRAY_TASK_ID]}'
"

mv -r 0* ~/projects/nhm/jmcdermo/spirals/helicocystis_straight/Re10000/


