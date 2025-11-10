# Analysis
This folder contains scripts for data extraction using pvpython and plotting

## `data_extraction.py`
This extracts velocity values for all z-points at three x-y locations in the wake of each organism at $x=0.05$ m, $0.1$ m and $0.15$ m over the last ten saved VTK timesteps (from $t=30$ s to $40$ s) as a time average, saved to csv files.

## `plotting.py`
This plots the data extracted from `data_extraction.py` for the three groups of organisms; the gogiids, the Helicocystis/Helicoplacus duo, and the edrioasteroids.

## `analysis.sh`
SLURM job to run both extraction and plotting.