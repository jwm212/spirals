#!/bin/bash
#SBATCH --array=0-4
#SBATCH --job-name=gp_Re5000
#SBATCH --partition=short
#SBATCH --cpus-per-task=1
#SBATCH --mem=8G

times=(0:7 7.1:14 14.1:21 21.1:28 28.1:36.4)

cd $SCRATCH/$SLURM_JOB_NAME

apptainer run --bind $SCRATCH:/mnt --pwd $SCRATCH/$SLURM_JOB_NAME ~/apps/openfoam_12.sif bash -c "
reconstructPar -time '${times[$SLURM_ARRAY_TASK_ID]}'
"

mv 0* ~/projects/nhm/jmcdermo/spirals/gogia_palmeri/Re5000/
mv postProcessing ~/projects/nhm/jmcdermo/spirals/gogia_palmeri/Re5000/
mv logs ~/projects/nhm/jmcdermo/spirals/gogia_palmeri/Re5000/


