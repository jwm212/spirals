#!/bin/bash
#SBATCH --array=0-4
#SBATCH --job-name=h_Re1000
#SBATCH --partition=medium
#SBATCH --cpus-per-task=1
#SBATCH --mem=8G

times=(0:0.5 0.6:1.1 1.2:1.7 1.8:2.3 2.4:2.7)

cd $SCRATCH/$SLURM_JOB_NAME

apptainer run --bind $SCRATCH:/mnt --pwd $SCRATCH/$SLURM_JOB_NAME ~/apps/openfoam_12.sif bash -c "
reconstructPar -time '${times[$SLURM_ARRAY_TASK_ID]}'
"

mv 0* ~/projects/nhm/jmcdermo/spirals/helicocystis/Re1000/
mv postProcessing ~/projects/nhm/jmcdermo/spirals/helicocystis/Re1000/
mv logs ~/projects/nhm/jmcdermo/spirals/helicocystis/Re1000/


