#!/bin/bash

#SBATCH --array=0-5
#SBATCH --partition=medium
#SBATCH --cpus-per-task=24
#SBATCH --mem=8G


cases=(v0.05 v0.1 v0.2 v0.3 v0.4 v0.5)
apptainer run --bind ~/projects/nhm/jmcdermo/:/mnt --pwd /mnt/spirals/stromatocystites/velocity/${cases[$SLURM_ARRAY_TASK_ID]} ~/apps/openfoam_12.sif bash -c "
decomposePar &&
mpirun --use-hwthread-cpus -n 24 --oversubscribe icoFoam -parallel | tee log.icoFoam &&
reconstructPar &&
foamLog log.icoFoam &&
foamToVTK"

# Remove processor dirs:
rm -rf ../${cases[$SLURM_ARRAY_TASK_ID]}/processor*

# plot residuals and save inside each case file in postProcessing/
echo "plotting residuals..."
cd ../${cases[$SLURM_ARRAY_TASK_ID]}
gnuplot ../scripts/residuals.gnu


#compress VTK files ready for transfer
cd $TMPDIR
echo "copying .vtk files..."
time cp ~/projects/nhm/jmcdermo/spirals/stromatocystites/velocity/${cases[$SLURM_ARRAY_TASK_ID]}/VTK/*.vtk .
echo "compressing VTK files..."
time tar -cvf VTKs.tar *.vtk
time pigz -p 24 VTKs.tar

mv VTKs.tar.gz ~/projects/nhm/jmcdermo/spirals/stromatocystites/velocity/${cases[$SLURM_ARRAY_TASK_ID]}/VTK
echo "done"
