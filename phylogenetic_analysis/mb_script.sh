#!/bin/bash

#SBATCH --partition=medium
#SBATCH --cpus-per-task=8
#SBATCH --mem=16G
# Request 8 MPI tasks (one per MPI rank)
#SBATCH --ntasks=8

echo "CPUs available: $SLURM_CPUS_PER_TASK"
echo "MPI tasks allocated: $SLURM_NTASKS"

# Use the Slurm-provided task count when launching MPI to avoid "not enough slots".
# The cluster reported hwloc_set_cpubind errors when mpirun attempted to bind ranks
# to CPU bitmaps. If `srun` isn't available/working on your system, disable OpenMPI
# cpu binding so Slurm (or the kernel) controls placement instead of hwloc.
# Set an MCA param to avoid hwloc binding attempts, then run mpirun with binding off.
export OMPI_MCA_hwloc_base_binding_policy=none
mpirun --bind-to none -n $SLURM_NTASKS mb-mpi metazoa_mb.nex

# If this still fails, try adding `--map-by slot` or removing `-n $SLURM_NTASKS`
# to let mpirun inherit Slurm's launch (or consult your cluster docs for the
# recommended MPI launcher/integration). Example fallback:
# mpirun --bind-to none --map-by slot -n $SLURM_NTASKS mb-mpi metazoa_ASR_ctenosis_mb.nex