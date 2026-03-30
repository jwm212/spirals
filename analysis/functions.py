# Created 13/03/2026
# Module containing functions for reading in a processing CFD data for plotting
import numpy as np
import pandas as pd
import csv
from scipy.signal import welch

def read_drag(taxon, A_frontal):
    # Read the forceCoeffs.dat file and extract Cd values from timestep 30 onwards, finds mean of those values,
    # and errors based on min and max values.
    filename = "../" + taxon + "/velocity/v0.1/postProcessing/forces/0/forceCoeffs.dat"
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
    mean_Cd = np.mean(Cd_list)*0.00024/A_frontal
    max_Cd = np.max(Cd_list)*0.00024/A_frontal
    min_Cd = np.min(Cd_list)*0.00024/A_frontal
    error_Cd = np.array([mean_Cd - min_Cd, max_Cd - mean_Cd])
    Cd_data = {"taxon": taxon,
               "mean": mean_Cd, 
               "error": error_Cd
               }
    return Cd_data

def calculate_x(taxon, A, V, Cd, r, R, f_calcite, U_0, rho_w, g, rho_calcite):
    # calcuates dimensionless number x/R for a range of f_calcite and U_0 values
    result = []
    for i in range(len(f_calcite)):
        for j in range(len(U_0)):
            F_d = 0.5*rho_w*Cd*A*U_0[j]**2 # calculate drag force (N)
            G = f_calcite[i]*V*g*(rho_calcite-rho_w) # Calculate apparent gravity (N)
            W = F_d/G # take dimensionless ratio
            xR = r*W/R # multiply by r/R to get dimensionless x/R
            
            result.append((taxon, f_calcite[i], U_0[j], xR))
    df = pd.DataFrame(result, columns=['taxon', 'f_calcite', 'U_0', 'xR'])
    return df

def read_FFT(taxon, L):
    # Reads in FFT data from paraview, removes negative frequencies and computes Strouhal number based
    # on characteristic length provided, assuming free stream velocity of 0.1m/s.
    file = '../' + taxon +'/velocity/v0.1/postProcessing/FFT.csv'
    with open(file) as f:
        freq = []
        Fx = []
        Fy = []

        reader = csv.DictReader(f, delimiter=',')
        for row in reader:
            freq.append(float(row['Frequency']))  # Access by column header instead of column number
            Fx.append(float(row['avg(U (1)):0']))  
            Fy.append(float(row['avg(U (1)):1']))  

        freq = np.array(freq)
        Fx = np.array(Fx)
        Fy = np.array(Fy)
        F = np.sqrt(Fx**2 + Fy**2) 
        # removing -ve frequencies
        freq_pos = freq[freq >= 0]
        F_pos = F[:len(freq_pos)]

        # Strouhal number: St = f*L/U
        U = 0.1 # free stream velocity
        strouhal = freq_pos*L/U
        taxon = np.array([taxon]*len(strouhal))
        FFT_final = np.array([taxon, strouhal, F_pos]).T
        df = pd.DataFrame(FFT_final, columns=['taxon', 'strouhal', 'FFT'])
        df['strouhal'] = df['strouhal'].astype(float)
        df['FFT'] = df['FFT'].astype(float)
        
        return df

def calc_residence_time(taxon, file, D, U_0): 
    # Reads in helicity data from paraview, calculates returns non-dimensional residence time t*
    dir = '../' + taxon +'/velocity/v0.1/postProcessing/'
    with open(dir + file) as f:
        #row_count = sum(1 for row in f)
        H = []

        reader = csv.DictReader(f, delimiter=',')
        for row in reader:
            H.append(float(row['Helicity']))  # Access by column header instead of column number

        H = np.array(H)
        residence_time = H*D/U_0
        #residence_velocity = D/residence_time
        return residence_time

def calc_FFT(taxon, file, L):
    dir = '/home/jmcdermo/projects/nhm/jmcdermo/spirals/' + taxon + '/video/base_case/postProcessing/'
    with open(dir + file) as f:
        v = []
        reader = csv.DictReader(f, delimiter=',')
        for row in reader:
            v.append(float(row['avg(U (1))']))

    v = np.array(v)*100
    v = np.abs(v[750:])
    t = np.arange(30,60+0.04,0.04) #final 30 seconds of 60s run
    fs = 1/0.04

    f, pxx = welch(v, fs)
    U = 0.1
    st = f*L/U
    # Find the index of the maximum y value
    max_pxx_index = np.argmax(pxx)

    # Retrieve the x value at that index
    max_f_value = f[max_pxx_index]

    print("Peak occurs at :", max_f_value, " Hz")

    return {'frequency': f, 'strouhal': st, 'psd': pxx}


## UNDER DEV ###
#def gamma_fit(data):
    #fit_alpha, fit_loc, fit_beta=stats.gamma.fit(data)
    #gamma_pdf = stats.gamma.pdf(np.sort(data), fit_alpha, loc=fit_loc, scale=fit_beta)
#    gamma_pdf = (data**(a-1)*np.exp(-data))/scipy.special.gamma(a)
#    return gamma_pdf


# makes module run in on its own
#if __name__ == "__main__":
#    import sys
#    fib(int(sys.argv[1]))