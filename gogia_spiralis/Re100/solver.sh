#!/bin/bash
#SBATCH --job-name=gs_Re100
#SBATCH --partition=short
#SBATCH --cpus-per-task=24
#SBATCH --mem=8G

mkdir $SCRATCH/$SLURM_JOB_NAME
cp -r 0 constant system reconstruct.sh $SCRATCH/$SLURM_JOB_NAME/
cd $SCRATCH/$SLURM_JOB_NAME

apptainer run --bind $SCRATCH:/mnt --pwd $SCRATCH/$SLURM_JOB_NAME ~/apps/openfoam_12.sif bash -c "
decomposePar &&
mpirun --use-hwthread-cpus -n 24 --oversubscribe icoFoam -parallel | tee log.icoFoam &&
postProcess -func vorticity &&
foamLog log.icoFoam 
"
sbatch reconstruct.sh


