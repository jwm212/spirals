#!/bin/bash
#SBATCH --job-name=gp_Re500
#SBATCH --partition=short
#SBATCH --cpus-per-task=32
#SBATCH --mem=8G

mkdir $SCRATCH/$SLURM_JOB_NAME
cp -r 0 constant system reconstruct.sh $SCRATCH/$SLURM_JOB_NAME/
cd $SCRATCH/$SLURM_JOB_NAME

apptainer run --bind $SCRATCH:/mnt --pwd $SCRATCH/$SLURM_JOB_NAME ~/apps/openfoam_12.sif bash -c "
decomposePar &&
mpirun --use-hwthread-cpus -n 32 --oversubscribe icoFoam -parallel | tee log.icoFoam &&
postProcess -func vorticity &&
foamLog log.icoFoam 
"
sbatch reconstruct.sh


