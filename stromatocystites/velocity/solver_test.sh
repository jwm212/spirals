#!/bin/bash

#SBATCH --partition=short
#SBATCH --cpus-per-task=24
#SBATCH --mem=8G


apptainer run --bind ~/projects/nhm/jmcdermo/:/mnt --pwd /mnt/spirals/stromatocystites/velocity/v0.1 ~/apps/openfoam_12.sif bash -c "
decomposePar &&
mpirun --use-hwthread-cpus -n 24 --oversubscribe icoFoam -parallel | tee log.icoFoam &&
reconstructPar &&
foamLog log.icoFoam &&
foamToVTK"

# Remove processor dirs:
rm -rf v0.1/processor*

#compress VTK files ready for transfer
cd $TMPDIR
echo "copying .vtk files"
time cp ~/projects/nhm/jmcdermo/spirals/stromatocystites/velocity/v0.1/VTK/*.vtk .
echo "compressing VTK files"
time tar -cvf VTKs.tar *.vtk
time pigz -p 24 VTKs.tar

mv VTKs.tar.gz ~/projects/nhm/jmcdermo/spirals/stromatocystites/velocity/v0.1/VTK/
