#!/bin/bash

#SBATCH --array=0-4 
#SBATCH --partition=short
#SBATCH --cpus-per-task=1
#SBATCH --mem=4G

# Defining taxon (use parameters.py object name)
taxon=(Gogia_palmeri)
# Defining array of cases
cases=(Re100 Re500 Re1000 Re5000 Re10000)
#cases=(Re500)

pvbatch -u probe.py "${taxon[0]}" "${cases[$SLURM_ARRAY_TASK_ID]}"