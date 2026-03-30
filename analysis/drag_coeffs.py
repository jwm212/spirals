print("importing modules...")
import numpy as np
import paraview
import glob
import os
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import csv
import gc

# Extract Cd from timestep 30 to the last timestep (excluding header lines)
def extract_coeffs(filename):
    # Read the forceCoeffs.dat file and extract Cd values from timestep 50 onwards
    with open(filename, 'r') as file:
        lines = file.readlines()
        if not lines:
            raise ValueError("The file is empty.")
        data_lines = lines[29:]  # take data from 30s onwards
        Cd_list = []
        for line in data_lines:
            if line.strip() and not line.startswith('#'):
                parts = line.split()
                if len(parts) > 2:
                    Cd_list.append(float(parts[2]))
        return np.array(Cd_list)

taxon = np.array(["gogia_palmeri", "gogia_spiralis", "stromatocystites",  "kailidiscus", "helicocystis_straight", "helicocystis", "helicoplacus"])
arr = np.arange(0,len(taxon),1)
max_Cd, mean_Cd, min_Cd = (np.zeros(len(taxon)) for _ in range(3))
errors_Cd = np.zeros((2, len(taxon)))  # 2 rows for lower and upper uncertainty
errors_Cl = np.zeros((2, len(taxon)))

# Frontal areas in m^2 for each taxon
A_frontal = np.array([0.000792, 0.000284, 0.00114, 0.00106, 0.00024, 0.0000331, 0.000443]) # frontal area for Helicocystis straight is already defined correctly in its controlDict: 0.00024/0.00024 = 1.

# Extracting data and rescaling to correct frontal area
for i in arr:
    file = "../" + taxon[i] + "/velocity/v0.1/postProcessing/forces/0/forceCoeffs.dat"
    print(file)
    Cd_data = extract_coeffs(file)
    #Cl_data = extract_coeffs(file)[1]
    max_Cd[i], mean_Cd[i], min_Cd[i] = Cd_data.max(), Cd_data.mean(), Cd_data.min()
    #rescaling to measured frontal area (original area 0.00024 m^2):
    max_Cd[i], mean_Cd[i], min_Cd[i] = max_Cd[i]*0.00024/A_frontal[i], mean_Cd[i]*0.00024/A_frontal[i], min_Cd[i]*0.00024/A_frontal[i]  
    print(f"Case {taxon[i]}: Cd {mean_Cd[i]}")
    errors_Cd[[0],i] = mean_Cd[i] - min_Cd[i]
    errors_Cd[[1],i] = max_Cd[i] - mean_Cd[i]
    print(f"Cd uncertainty: {errors_Cd[:,i]}")

# Calculating percentage difference:
Cd_diff = np.zeros(len(taxon))
Cd_reldiff = np.zeros(len(taxon))
for i in range(len(mean_Cd)-1):
    Cd_diff[i] = (mean_Cd[i]/mean_Cd[-1]-1)*100
    Cd_reldiff[i+1] = (mean_Cd[i+1]/mean_Cd[i]-1)*100 



print(mean_Cd)
print(errors_Cd)
plt.rcParams.update({'font.size': 8})
# replaced plotting block to alternate marker and color per point
fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(6, 4), dpi=300)
pl_taxa = np.array(["Gogia palmeri", "Gogia spiralis", "Stromatocystites",  "Kailidiscus", "Helicocystis straight", "Helicocystis", "Helicoplacus"])
labels = [r"$\it{Gogia}$ $\it{palmeri}$", r"$\it{Gogia}$ $\it{spiralis}$", r"$\it{Stromatocystites}$",  r"$\it{Kailidiscus}$", r"$\it{Helicocystis}$ (straight)", r"$\it{Helicocystis}$", r"$\it{Helicoplacus}$"]
x = np.arange(len(pl_taxa))

# alternating markers and colours: even -> 'x' blue, odd -> 'o' orange
markers = ['x', 'o', 'x', 'o', 'x','o', 'o']
colors = ['C0', 'C1', 'C0', 'C1', 'C0', 'C1', 'red',]

for i in range(len(pl_taxa)):
    xi = [x[i]]
    yi = [mean_Cd[i]]
    err = errors_Cd[:, i].reshape(2, 1)  # shape (2,1) matches one y value

    ax.scatter(xi, yi, marker=markers[i], color=colors[i], s=20, zorder=3)
    ax.errorbar(xi, yi, yerr=err, fmt='none', ecolor=colors[i], capsize=3, zorder=2)

ax.set_xticks(x)
ax.set_xticklabels(labels, rotation=30, ha='right')

## vertical lines to separate groups ##
n_groups = 6
index = np.arange(n_groups)
ax.axvline(index[1]+0.5, color='gray', linestyle='dashed')
ax.axvline(index[3]+0.5, color='gray', linestyle='dashed')

## legend ##
# build a deduplicated legend (one entry per location)
handles, labels = ax.get_legend_handles_labels()
by_label = {}
for h, l in zip(handles, labels):
    if l not in by_label:
        by_label[l] = h

# custom marker legend entries for 'x' and 'o'
x_handle = Line2D([0], [0], color='C0', marker='x', linestyle='None', markersize=8, label='straight (5-fold)')
o_handle1 = Line2D([0], [0], color='red', marker='o', linestyle='None', markersize=8, label='spiral (3-fold)')
o_handle2 = Line2D([0], [0], color='C1', marker='o', linestyle='None', markersize=8, label='spiral (5-fold)')

# combine location handles + linestyle handles
all_handles = list(by_label.values()) + [x_handle, o_handle1, o_handle2]
all_labels = list(by_label.keys()) + ['straight', 'spiral (3-fold)', 'spiral (5-fold)']

fig.legend(
    all_handles,
    all_labels,
    loc='upper right',
)


ax.set_ylabel(r'Mean $C_d$')
plt.legend()
plt.tight_layout()
plt.savefig('drag_coeffs_taxa.pdf')#, bbox_inches='tight')


