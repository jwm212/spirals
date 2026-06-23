#!/bin/bash

#SBATCH --array=0
#SBATCH --partition=short
#SBATCH --cpus-per-task=1
#SBATCH --mem=4G


# Defining taxon (use parameters.py object name)
taxon=(Helicocystis_straight)
# Defining array of cases
#cases=(Re100 Re500 Re1000 Re5000 Re10000)
cases=(Re500)

#cases=(Re10000)

# Defining array of times to be used for torque data - ignoring first flow_through_time.
#time_range_min=((64 52 65 52 65) ((64 52 65 52 65)) (108 108 108 108 108))
#time_range_min=(65)
#time_range_max=(321 257 324 259 324)
#time_range_max=(324)

pvbatch -u torque.py "${taxon[0]}" "${cases[$SLURM_ARRAY_TASK_ID]}"