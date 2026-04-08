#!/bin/bash

#SBATCH --array=0
#SBATCH --partition=short
#SBATCH --cpus-per-task=1
#SBATCH --mem=4G

rm -rf ./processor*