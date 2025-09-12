# TODO: calculate percentage difference from last resolution and visualise on the plot

import numpy as np
import matplotlib.pyplot as plt

#def extract_coeffs(filename):
#    # A function to read the Cd and Cl values from the last timestep of a forceCoeffs.dat file
#    with open(filename, 'r') as file:
#        lines = file.readlines()
#        if not lines:
#            raise ValueError("The file is empty.")
#        last_line = lines[-1].strip()#

    # Split the last line by whitespace or comma
#    if ',' in last_line:
#        data = last_line.split(',')
#    else:
#        data = last_line.split()
    
#    data = np.array(data, dtype=float)
#    Cd = data[2]
#    Cl = data[3]
#    # Convert to float array
#    return np.array([Cd, Cl])

# Extract Cd and Cl data from timestep 50 to the last timestep (excluding header lines)
def extract_coeffs(filename):
    # Read the forceCoeffs.dat file and extract Cd values from timestep 50 onwards
    with open(filename, 'r') as file:
        lines = file.readlines()
        if not lines:
            raise ValueError("The file is empty.")
        data_lines = lines[29:]  # take data from 30s onwards
        Cd_list = []
        Cl_list = []
        for line in data_lines:
            if line.strip() and not line.startswith('#'):
                parts = line.split()
                if len(parts) > 2:
                    Cd_list.append(float(parts[2]))
                    Cl_list.append(float(parts[3]))
        return np.array((Cd_list, Cl_list))

    # Usage example:
    # Cd_data, Cl_data = extract_coeffs(file)

cases = np.array(["deg0", "deg45", "deg90", "deg135", "deg180"])
arr = np.arange(0,len(cases),1)
# Creating dummy arrays to read data into:
max_Cd, mean_Cd, min_Cd, max_Cl, mean_Cl, min_Cl = (np.zeros(len(cases)) for _ in range(6))
# Creating arrays to store uncertainties:
errors_Cd = np.zeros((2, len(cases)))  # 2 rows for lower and upper uncertainty
errors_Cl = np.zeros((2, len(cases)))

# Extracting data:
for i in arr:
    file = "../" + cases[i] + "/postProcessing/forces/0/forceCoeffs.dat"
    print(file)
    Cd_data, Cl_data = extract_coeffs(file)
    #Cl_data = extract_coeffs(file)[1]
    max_Cd[i], mean_Cd[i], min_Cd[i] = Cd_data.max(), Cd_data.mean(), Cd_data.min()
    max_Cl[i], mean_Cl[i], min_Cl[i] = Cl_data.max(), Cl_data.mean(), Cl_data.min()
    
#    max_Cd[i] = np.max(Cd_data)
#    mean_Cd[i] = np.mean(Cd_data)
#    min_Cd[i] = np.min(Cd_data)
#    max_Cl[i] = np.max(Cl_data)
#    mean_Cl[i] = np.mean(Cl_data)
#    min_Cl[i] = np.min(Cl_data)
    print(f"Case {cases[i]}: Cd {mean_Cd[i]}, Cl {mean_Cl[i]}")
    errors_Cd[[0],i] = mean_Cd[i] - min_Cd[i]
    errors_Cd[[1],i] = max_Cd[i] - mean_Cd[i]
    errors_Cl[[0],i] = mean_Cl[i] - min_Cl[i]
    errors_Cl[[1],i] = max_Cl[i] - mean_Cl[i]
    print(f"Cd uncertainty: {errors_Cd[:,i]}")
    print(f"Cl uncertainty: {errors_Cl[:,i]}")

# Calculating percentage difference:
Cd_diff = np.zeros(len(cases))
#Cd_diff_errors = np.zeros((2,len(cases)))
#Cd_reldiff_errors = np.zeros((2,len(cases)))
Cd_reldiff = np.zeros(len(cases))
Cl_diff = np.zeros(len(cases))
#Cl_diff_errors = np.zeros((2,len(cases)))
Cl_reldiff = np.zeros(len(cases))
#Cl_reldiff_errors = np.zeros((2,len(cases)))
for i in range(len(mean_Cd)-1):
    Cd_diff[i] = (mean_Cd[i]/mean_Cd[-1]-1)*100
    #Cd_diff_errors[[0],i] = (errors_Cd[[0],i]/errors_Cd[[0],-1],-1)*100  # Calculate error in percentage
    #Cd_diff_errors[[1],i] = (errors_Cd[[1],i]/errors_Cd[[1],-1]-1)*100  # Calculate error in percentage
    Cd_reldiff[i+1] = (mean_Cd[i+1]/mean_Cd[i]-1)*100  # old: rel % diff: (Cd[i+1]/Cd[i]-1)*100
    #Cd_reldiff_errors[[0],i+1] = (errors_Cd[[0],i+1]/errors_Cd[[0],i])*100  # Calculate error in percentage
    #Cd_reldiff_errors[[1],i+1] = (errors_Cd[[1],i+1]/errors_Cd[[1],i])*100 
    
    Cl_diff[i] = (mean_Cl[i]/mean_Cl[-1]-1)*100
    #Cl_diff_errors[i] = (errors_Cl[0,i]/errors_Cl[-1]-1)*100  # Calculate error in percentage
    Cl_reldiff[i+1] = (mean_Cl[i+1]/mean_Cl[i]-1)*100
    #Cl_reldiff_errors[i+1] = (errors_Cl[i+1]/errors_Cl[i])*100  # Calculate error in percentage

# Plotting:
pl_cases = [0, 45, 90, 135, 180]
#xlabels = ['4','6','8','10','12','14']
print(pl_cases[1:])
print(Cd_reldiff)

plt.rcParams.update({'font.size': 8})
fig, axs = plt.subplots(nrows=1, ncols=1, figsize=(5, 4), dpi=300)

axs.scatter(pl_cases, mean_Cd, label=r'Mean $C_d$')
axs.plot(pl_cases, mean_Cd, linewidth=0.5, c='C0')
axs.errorbar(pl_cases, mean_Cd, yerr=errors_Cd, fmt='o', capsize=3, c='C0')
axs.scatter(pl_cases, mean_Cl, c='orange', marker='x',label=r'Mean $C_l$')
axs.plot(pl_cases, mean_Cl, c='orange', linewidth=0.5)
axs.errorbar(pl_cases, mean_Cl, yerr=errors_Cl, fmt='x', capsize=3, color='orange')
#axs[0].set_title('Force coefficients')
axs.set_xlabel('distance downstream (L)')
axs.set_xticks(np.arange(240,960,120))
#axs.set_xticklabels(xlabels)
axs.legend(loc='center right')
#ax2 = axs[0].twinx()
#ax2.scatter(pl_cases, mean_Cl, c='orange', marker='x')
#ax2.plot(pl_cases, mean_Cl, c='orange', linewidth=0.5)
#ax2.errorbar(pl_cases, mean_Cl, yerr=errors_Cl, fmt='x', capsize=3, color='orange', label='Uncertainty')
#ax2.set_xlabel('downstream length')
#ax2.set_ylabel(r'$C_l$')
#ax2.set_xticks(np.arange(240,960,120))
#ax2.set_xticklabels(xlabels)

#axs[1].set_title('Percentage difference')
#axs[1].scatter(pl_cases,Cd_diff,label=r'$C_d$')
#axs[1].plot(pl_cases,Cd_diff, linewidth=0.5)
#axs[0].errorbar(pl_cases, Cd_diff, yerr=Cd_diff_errors, fmt='o', capsize=3, label='Uncertainty', color='gray')
#axs[1].scatter(pl_cases,Cl_diff, marker ='x', c='orange', label=r'$C_l$')
#axs[1].plot(pl_cases,Cl_diff, c='orange', linewidth=0.5)
#axs[1].set_yscale('log')
#axs[1].set_ylabel('% difference')
#axs[1].set_xlabel('downstream length')
#axs[1].set_xticks(np.arange(240,960,120))
#axs[1].set_xticklabels(xlabels)
#axs[1].legend(loc='lower right')

#axs[2].set_title('Relative Percentage difference')
#axs[2].scatter(pl_cases,Cd_reldiff,label=r'$C_d$')
#axs[2].plot(pl_cases,Cd_reldiff, linewidth=0.5)
#axs[2].scatter(pl_cases,Cl_reldiff, marker ='x', c='orange', label=r'$C_l$')
#axs[2].plot(pl_cases,Cl_reldiff, c='orange', linewidth=0.5)
#axs[2].set_yscale('log')
#axs[2].set_ylabel('% difference')
#axs[2].set_xlabel('downstream length')
#axs[2].set_xticks(np.arange(240,960,120))
#axs[2].set_xticklabels(xlabels)
#axs[2].legend(loc='lower right')

#handles, labels = axs.get_legend_handles_labels()
#fig.legend(
#    handles, labels,
#    loc='center right'
    #bbox_to_anchor=(1.02, 0.5),  # adjust this to move legend further right/left
    #borderaxespad=0,
    #title='Locations'
#)

# Make room for the legend on the right
#plt.subplots_adjust(right=0.82)  # Adjust as needed

#fig.tight_layout()

plt.savefig("../drag_lift_coeffs.pdf")