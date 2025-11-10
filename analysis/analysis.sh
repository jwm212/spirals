#!/bin/bash

#SBATCH --partition=short
#SBATCH --cpus-per-task=1
#SBATCH --mem=16G


pvpython data_extraction.py
python plotting.py