print("importing modules...")
import numpy as np
import paraview
import glob
import os
import matplotlib.pyplot as plt
import csv
import gc

def U_read(file):
    with open(file) as f:
        #row_count = sum(1 for row in f)
        x = []
        u = []
        v = []
        w = []
        reader = csv.DictReader(f, delimiter=',')
        for row in reader:
            x.append(float(row['arc_length']))
            u.append(float(row['U_average:0']))  # Access by column header instead of column number
            v.append(float(row['U_average:1']))
            w.append(float(row['U_average:2']))
            
        x = np.array(x)
        u = np.array(u)
        #v = np.array(v)
        #w = np.array(w)
        
        #x = x*100  #convert to cm
        #Umag = np.sqrt((u**2)+(v**2)+(w**2))*1000
        #print(Umag.shape)
        U_final = np.array((x, u*100))#Umag
        
        return U_final


taxon = np.array(["gogia_palmeri", "helicoplacus", "stromatocystites",  "gogia_spiralis", "helicocystis", "kailidiscus"])
arr = np.arange(0,len(taxon),1)
print("taxa:", taxon)
L = np.array([0.13, 0.04, 0.03, 0.065, 0.012, 0.03]) #characterstic length in mm of each taxon.
files = np.array(['Uloc_1_t_avrgd.csv', 'Uloc_2_t_avrgd.csv', 'Uloc_3_t_avrgd.csv'])
#Uloc1 = np.empty((2,1001))
#Uloc1 = U_extract('n80/Uloc1.csv')

plt.rcParams.update({'font.size': 10})
fig, axs = plt.subplots(1, 3)
fig.set_figheight(4) #height and width in inches. Width of A4 sheet is 8.27 in
fig.set_figwidth(7)
fig.set_dpi(300)

titles = ['Gogiids', 'Helicoplaoids', 'Edrioasteroids']
distance = ["0.05 m", "0.1 m", "0.15 m"]
#for i in range(len(files)):
#    col = i%3
#    dir = '../'+cases[i]+'/postProcessing/'
#    axs[col].set_title(locs[i], fontsize=10)

#    for j in arr:
#        data = U_extract(dir+files[i])
#        axs[col].plot(data[1], data[0], linewidth=1, label=f'{cases[j]}')
# define linestyles per taxon name (defaults to solid)
linestyles = {
    'gogia_palmeri': '-',
    'gogia_spiralis': '--',
    'helicoplacus': '-',
    'helicocystis': '--',
    'stromatocystites': '-',
    'kailidiscus': '--'
}

# define a fixed colour for each location (Location 1,2,3)
# these will be used for both solid and dashed lines so each location keeps the same colour
colors = ['C0', 'C1', 'C2']  # change to any 3 distinct colours you prefer

for i in range(len(taxon)):
    col = i % 3
    axs[col].set_title(titles[col], fontsize=10)

    for j in range(len(files)):
        dir = '../' + taxon[i] + '/velocity/v0.1/postProcessing/'
        file_path = dir + files[j]
        print(f"Loading: {file_path}")
        data = U_read(dir + files[j])
        print(f"First 5 u values for {taxon[i]}: {data[1][:5]}\n")
        print(f"{taxon[i]} characteristic length L: {L[i]} m")

        linestyle = linestyles.get(taxon[i], '-')  # default solid if not listed
        axs[col].plot(data[1], data[0]/L[i],
                      linestyle=linestyle,
                      color=colors[j],
                      linewidth=1,
                      label=f'{distance[j]}')

for ax in axs.flat:
    ax.set(xlabel='u (cm/s)', ylabel='z/L')
    ax.set_xticks([0,5,10])
    
for ax in axs.flat:
    ax.label_outer()
    
# build a deduplicated legend (one entry per location)
handles, labels = axs[0].get_legend_handles_labels()
by_label = {}
for h, l in zip(handles, labels):
    if l not in by_label:
        by_label[l] = h

fig.legend(
    list(by_label.values()),
    list(by_label.keys()),
    loc='center right',
    title='Locations'
)

# Make room for the legend on the right
plt.subplots_adjust(right=0.82)  # Adjust as needed
plt.savefig('U_average_X_profiles.pdf')