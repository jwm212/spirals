#!/bin/bash
#SBATCH --array=0-4
#SBATCH --job-name=gs_Re10000
#SBATCH --partition=short
#SBATCH --cpus-per-task=1
#SBATCH --mem=8G

times=(0:0.9 0.91:1.8 1.81:2.7 2.71:3.6 3.61:4.55)

cd $SCRATCH/$SLURM_JOB_NAME

apptainer run --bind $SCRATCH:/mnt --pwd $SCRATCH/$SLURM_JOB_NAME ~/apps/openfoam_12.sif bash -c "
reconstructPar -time '${times[$SLURM_ARRAY_TASK_ID]}'
"

mv 0* 1* 2* 3* 4* 5* 6* 7* 8* 9* ~/projects/nhm/jmcdermo/spirals/gogia_spiralis/Re10000/
mv postProcessing ~/projects/nhm/jmcdermo/spirals/gogia_spiralis/Re10000/
mv logs ~/projects/nhm/jmcdermo/spirals/gogia_spiralis/Re10000/


