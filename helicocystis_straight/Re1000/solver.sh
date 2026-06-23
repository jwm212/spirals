#!/bin/bash
#SBATCH --job-name=h_st_Re1000
#SBATCH --partition=medium
#SBATCH --cpus-per-task=24
#SBATCH --mem=8G



apptainer run --bind ~/projects/nhm/jmcdermo/:/mnt --pwd /mnt/spirals/helicocystis_straight/Re1000 ~/apps/openfoam_12.sif bash -c "
decomposePar &&
mpirun --use-hwthread-cpus -n 24 --oversubscribe icoFoam -parallel | tee log.icoFoam &&
postProcess -func vorticity &&
foamLog log.icoFoam &&
reconstructPar
"

rm -rf processor*

# plot residuals and save inside each case file in postProcessing/
echo "plotting residuals..."
gnuplot residuals.gnu
