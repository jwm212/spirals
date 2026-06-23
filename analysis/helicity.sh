#!/bin/bash

#SBATCH --array=0-4
#SBATCH --partition=short
#SBATCH --cpus-per-task=1
#SBATCH --mem=4G

# Defining taxon (use parameters.py object name). REMEMBER TO UPDATE BOX IN helicity.py
taxon=(Helicocystis_straight)
# Defining array of cases
cases=(Re100 Re500 Re1000 Re5000 Re10000)


#mpirun --use-hwthread-cpus -n 16 --oversubscribe pvbatch -u stromat_helicity.py "${cases[$SLURM_ARRAY_TASK_ID]}" "${time_range_min[$SLURM_ARRAY_TASK_ID]}" "${time_range_max[$SLURM_ARRAY_TASK_ID]}"
pvbatch -u helicity.py "${taxon[0]}" "${cases[$SLURM_ARRAY_TASK_ID]}"