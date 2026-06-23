#!/bin/bash
#SBATCH --array=0-4
#SBATCH --job-name=gp_Re500
#SBATCH --partition=short
#SBATCH --cpus-per-task=1
#SBATCH --mem=8G

times=(0:70 71:140 141:210 211:280 281:364)

cd $SCRATCH/$SLURM_JOB_NAME

apptainer run --bind $SCRATCH:/mnt --pwd $SCRATCH/$SLURM_JOB_NAME ~/apps/openfoam_12.sif bash -c "
reconstructPar -time '${times[$SLURM_ARRAY_TASK_ID]}'
"

mv 0* ~/projects/nhm/jmcdermo/spirals/gogia_palmeri/Re500/
mv postProcessing ~/projects/nhm/jmcdermo/spirals/gogia_palmeri/Re500/
mv logs ~/projects/nhm/jmcdermo/spirals/gogia_palmeri/Re500/


