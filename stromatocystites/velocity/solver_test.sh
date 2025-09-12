#!/bin/bash

#SBATCH --partition=short
#SBATCH --cpus-per-task=24
#SBATCH --mem=8G


apptainer run --bind ~/projects/nhm/jmcdermo/:/mnt --pwd /mnt/spirals/stromatocystites/velocity/v0.5 ~/apps/openfoam_12.sif bash -c "
decomposePar &&
mpirun --use-hwthread-cpus -n 24 --oversubscribe icoFoam -parallel | tee log.icoFoam &&
reconstructPar &&
foamLog log.icoFoam &&
foamToVTK"

# Remove processor dirs:
rm -rf v0.5/processor*

# plot residuals and save inside each case file in postProcessing/
echo "plotting residuals..."
cd ../v0.5
gnuplot ../scripts/residuals.gnu

#compress VTK files ready for transfer
cd $TMPDIR
echo "copying .vtk files"
time cp ~/projects/nhm/jmcdermo/spirals/stromatocystites/velocity/v0.5/VTK/*.vtk .
echo "compressing VTK files"
time tar -cvf VTKs.tar *.vtk
time pigz -p 24 VTKs.tar

mv VTKs.tar.gz ~/projects/nhm/jmcdermo/spirals/stromatocystites/velocity/v0.5/VTK/
