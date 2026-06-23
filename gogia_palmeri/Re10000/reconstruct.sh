#!/bin/bash
#SBATCH --array=0-4
#SBATCH --job-name=gp_Re10000
#SBATCH --partition=short
#SBATCH --cpus-per-task=1
#SBATCH --mem=8G

times=(0:4 4.05:8 8.05:12 12.05:16 16.05:18.2)

cd $SCRATCH/$SLURM_JOB_NAME

apptainer run --bind $SCRATCH:/mnt --pwd $SCRATCH/$SLURM_JOB_NAME ~/apps/openfoam_12.sif bash -c "
reconstructPar -time '${times[$SLURM_ARRAY_TASK_ID]}'
"

mv 0* ~/projects/nhm/jmcdermo/spirals/gogia_palmeri/Re10000/
mv postProcessing ~/projects/nhm/jmcdermo/spirals/gogia_palmeri/Re10000/
mv logs ~/projects/nhm/jmcdermo/spirals/gogia_palmeri/Re10000/


