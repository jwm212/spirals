#!/bin/bash
#SBATCH --job-name=h_st_Re500
#SBATCH --partition=medium
#SBATCH --cpus-per-task=48
#SBATCH --mem=8G

mkdir $SCRATCH/$SLURM_JOB_NAME
cp -r 0 constant system reconstructPar.sh $SCRATCH/$SLURM_JOB_NAME/
cd $SCRATCH/$SLURM_JOB_NAME

apptainer run --bind $SCRATCH:/mnt --pwd $SCRATCH/$SLURM_JOB_NAME ~/apps/openfoam_12.sif bash -c "
decomposePar &&
mpirun --use-hwthread-cpus -n 48 --oversubscribe icoFoam -parallel | tee log.icoFoam &&
postProcess -func vorticity &&
foamLog log.icoFoam 
"
sbatch reconstructPar.sh


# plot residuals and save inside each case file in postProcessing/
echo "plotting residuals..."
gnuplot residuals.gnu
