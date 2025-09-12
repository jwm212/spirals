#!/bin/bash

#SBATCH --array=0-4
#SBATCH --partition=short
#SBATCH --cpus-per-task=24
#SBATCH --mem=6G


cases=(deg0 deg45 deg90 deg135 deg180)
apptainer run --bind ~/projects/nhm/jmcdermo/:/mnt --pwd /mnt/spirals/stromatocystites/orientation/${cases[$SLURM_ARRAY_TASK_ID]} ~/apps/openfoam_12.sif bash -c "
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
time cp ~/projects/nhm/jmcdermo/spirals/stromatocystites/orientation/${cases[$SLURM_ARRAY_TASK_ID]}/VTK/*.vtk .
echo "compressing VTK files..."
time tar -cvf VTKs.tar *.vtk
time pigz -p 24 VTKs.tar

mv VTKs.tar.gz ~/projects/nhm/jmcdermo/spirals/stromatocystites/orientation/${cases[$SLURM_ARRAY_TASK_ID]}/VTK
echo "done"
