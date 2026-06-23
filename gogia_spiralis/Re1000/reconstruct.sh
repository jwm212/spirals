#!/bin/bash
#SBATCH --array=0-4
#SBATCH --job-name=gs_Re1000
#SBATCH --partition=short
#SBATCH --cpus-per-task=1
#SBATCH --mem=8G

times=(0:9 9.1:18 18.1:27 27.1:36 36.1:45)

cd $SCRATCH/$SLURM_JOB_NAME

apptainer run --bind $SCRATCH:/mnt --pwd $SCRATCH/$SLURM_JOB_NAME ~/apps/openfoam_12.sif bash -c "
reconstructPar -time '${times[$SLURM_ARRAY_TASK_ID]}'
"

mv 0* 1* 2* 3* 4* 5* 6* 7* 8* 9* ~/projects/nhm/jmcdermo/spirals/gogia_spiralis/Re1000/
mv postProcessing ~/projects/nhm/jmcdermo/spirals/gogia_spiralis/Re1000/
mv logs ~/projects/nhm/jmcdermo/spirals/gogia_spiralis/Re1000/


