#!/bin/bash
#SBATCH --array=0-4
#SBATCH --job-name=gp_Re100
#SBATCH --partition=medium
#SBATCH --cpus-per-task=1
#SBATCH --mem=8G

times=(0:400 405:800 805:1200 1205:1500 1505:1820)

cd $SCRATCH/$SLURM_JOB_NAME

apptainer run --bind $SCRATCH:/mnt --pwd $SCRATCH/$SLURM_JOB_NAME ~/apps/openfoam_12.sif bash -c "
reconstructPar -time '${times[$SLURM_ARRAY_TASK_ID]}'
"

mv 0* ~/projects/nhm/jmcdermo/spirals/gogia_palmeri/Re100/
mv postProcessing ~/projects/nhm/jmcdermo/spirals/gogia_palmeri/Re100/
mv logs ~/projects/nhm/jmcdermo/spirals/gogia_palmeri/Re100/


