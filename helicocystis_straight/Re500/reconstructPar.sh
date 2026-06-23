#!/bin/bash
#SBATCH --array=0-4
#SBATCH --job-name=h_st_Re500
#SBATCH --partition=short
#SBATCH --cpus-per-task=1
#SBATCH --mem=8G

times=(0:1 1.01:2 2.01:3 3.01:4 4.01:5.4)

cd $SCRATCH/$SLURM_JOB_NAME

apptainer run --bind $SCRATCH:/mnt --pwd $SCRATCH/$SLURM_JOB_NAME ~/apps/openfoam_12.sif bash -c "
reconstructPar -time '${times[$SLURM_ARRAY_TASK_ID]}'
"

mv 0* 1* 2* 3* 4* 5* 6* 7* 8* 9* ~/projects/nhm/jmcdermo/spirals/helicocystis_straight/Re500/
mv postProcessing ~/projects/nhm/jmcdermo/spirals/helicocystis_straight/Re500/
mv logs ~/projects/nhm/jmcdermo/spirals/helicocystis_straight/Re500/