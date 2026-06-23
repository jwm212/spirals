#!/bin/bash
#SBATCH --array=0-4
#SBATCH --job-name=gp_Re1000
#SBATCH --partition=short
#SBATCH --cpus-per-task=1
#SBATCH --mem=8G

times=(0:40 40.5:80 80.5:120 120.5:160 160.5:182)

cd $SCRATCH/$SLURM_JOB_NAME

apptainer run --bind $SCRATCH:/mnt --pwd $SCRATCH/$SLURM_JOB_NAME ~/apps/openfoam_12.sif bash -c "
reconstructPar -time '${times[$SLURM_ARRAY_TASK_ID]}'
"

mv 0* ~/projects/nhm/jmcdermo/spirals/gogia_palmeri/Re1000/
mv postProcessing ~/projects/nhm/jmcdermo/spirals/gogia_palmeri/Re1000/
mv logs ~/projects/nhm/jmcdermo/spirals/gogia_palmeri/Re1000/


