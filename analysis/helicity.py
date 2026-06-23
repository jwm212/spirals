# trace generated using paraview version 5.13.2
#import paraview
#paraview.compatibility.major = 5
#paraview.compatibility.minor = 13
import sys
import time
import parameters as par
start_time = time.time()
#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

name=sys.argv[1]
taxon = getattr(par, name)
Re = str(sys.argv[2])


# READING DATA
casefoam = OpenFOAMReader(registrationName='case.foam', FileName=f'/mnt/shared/projects/nhm/jmcdermo/spirals/{taxon.name}/{Re}/case.foam')
casefoam.SkipZeroTime = 0
cache = TemporalCache(Input=casefoam) # Create temporary cache to prevent re-reading of data
time1 = time.time()
elapsed_time = time1 - start_time
print("Opened dataset : " + f'/mnt/shared/projects/nhm/jmcdermo/spirals/{taxon.name}/{Re}/case.foam     (time = {elapsed_time} seconds)')


# EXTRACT TIME STEPS
print("Extracting time steps for time range: ", taxon.cfd[Re]["time_range"])
extractTimeSteps1 = ExtractTimeSteps(registrationName='ExtractTimeSteps1', Input=cache)
extractTimeSteps1.SelectionMode = 'Select Time Range'
extractTimeSteps1.TimeStepRange = taxon.cfd[Re]["time_range"]
extractTimeSteps1.TimeStepInterval = 10
elapsed_time1 = time.time() - time1
print(f"Extracted time steps     (time = {elapsed_time1} seconds)")
time1 = time.time()


# EXTRACT CELLS
extractCellsByRegion1 = ExtractCellsByRegion(registrationName='ExtractCellsByRegion1', Input=extractTimeSteps1)
extractCellsByRegion1.IntersectWith = 'Box'
# Stromatocystites:
#extractCellsByRegion1.IntersectWith.Position = [-0.026, -0.024, 0.015]
#extractCellsByRegion1.IntersectWith.Length = [0.042, 0.048, 0.019]
# Kailidiscus:
#extractCellsByRegion1.IntersectWith.Position = [-0.028, -0.028, 0.013]
#extractCellsByRegion1.IntersectWith.Length = [0.056, 0.056, 0.022]
# Helicocystis:
#extractCellsByRegion1.IntersectWith.Position = [-0.003, -0.003, 0]
#extractCellsByRegion1.IntersectWith.Length = [0.006, 0.006, 0.013]
# Gogia palmeri:
#extractCellsByRegion1.IntersectWith.Position = [-0.008, -0.008, 0.057]
#extractCellsByRegion1.IntersectWith.Length = [0.016, 0.016, 0.01]
# Gogia spiralis:
#extractCellsByRegion1.IntersectWith.Position = [-0.007, -0.007, 0.035]
#extractCellsByRegion1.IntersectWith.Length = [0.014, 0.014, 0.006]
elapsed_time2 = time.time() - time1
print(f"Extracted cells     (time = {elapsed_time2} seconds)")
time1 = time.time()


# RESAMPLE CELLS
resampleToImage1 = ResampleToImage(registrationName='ResampleToImage1', Input=extractCellsByRegion1)
# Edrios:
#resampleToImage1.SamplingDimensions = [20, 20, 15]
# Helicocystis:
resampleToImage1.SamplingDimensions = [20, 20, 40]
elapsed_time3 = time.time() - time1
print(f"Resampled cells     (time = {elapsed_time3} seconds)")
time1 = time.time()


# CALCULATE VORTICITY
gradient1 = Gradient(registrationName='Gradient1', Input=resampleToImage1)
gradient1.ScalarArray = ['POINTS', 'U']
gradient1.ComputeGradient = 0
gradient1.ComputeVorticity = 1
elapsed_time4 = time.time() - time1
print(f"Calculated vorticity     (time = {elapsed_time4} seconds)")
time1 = time.time()


# CALCULATE HELICITY
calculator1 = Calculator(registrationName='Calculator1', Input=gradient1)
calculator1.AttributeType = 'Point Data'
calculator1.ResultArrayName = 'Helicity'
calculator1.Function = 'dot(U, Vorticity)'
elapsed_time4 = time.time() - time1
print(f"Calculated helicity     (time = {elapsed_time4} seconds)")
time1 = time.time()


# PLOT OVER TIME
plot_time = PlotDataOverTime(Input=calculator1)
plot_time.OnlyReportSelectionStatistics = 0
UpdatePipeline(time=2.0, proxy=plot_time)
elapsed_time5 = time.time() - time1
print(f"Plotted over time     (time = {elapsed_time5} seconds)")
time1 = time.time()


# SAVE DATA
SaveData(f'/mnt/shared/projects/nhm/jmcdermo/spirals/{taxon.name}/{Re}/postProcessing/helicity_resampled.csv', 
        proxy=plot_time,
        FieldAssociation='Row Data',
        RowDataArrays=['N', 'Time', 'Helicity'])
elapsed_time6 = time.time() - time1
print(f"Saved data     (time = {elapsed_time6} seconds)")
time1 = time.time()
end_time = time.time()
print(f"Total runtime: {end_time - start_time} seconds")