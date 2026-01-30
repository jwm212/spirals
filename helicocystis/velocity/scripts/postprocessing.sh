#!/bin/bash


#SBATCH --partition=gpu
#SBATCH --cpus-per-task=1
#SBATCH --mem=16G


pvbatch xz_profile_trace_time_averaged.py
