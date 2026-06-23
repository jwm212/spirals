#!/bin/bash
#SBATCH --array=0-4
#SBATCH --job-name=h_Re5000
#SBATCH --partition=medium
#SBATCH --cpus-per-task=1
#SBATCH --mem=8G

times=(0:0.1 0.101:0.2 0.201:0.3 0.301:0.4 0.401:0.54)

cd $SCRATCH/$SLURM_JOB_NAME

apptainer run --bind $SCRATCH:/mnt --pwd $SCRATCH/$SLURM_JOB_NAME ~/apps/openfoam_12.sif bash -c "
reconstructPar -time '${times[$SLURM_ARRAY_TASK_ID]}'
"

mv 0* ~/projects/nhm/jmcdermo/spirals/helicocystis/Re5000/
mv postProcessing ~/projects/nhm/jmcdermo/spirals/helicocystis/Re5000/
mv logs ~/projects/nhm/jmcdermo/spirals/helicocystis/Re5000/


