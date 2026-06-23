'''
This pvpython script, for a given taxon in parameters.py:
- reads in case.foam, 
- extracts timesteps after the first flow_through_time
- probes velocity at a point 5L downstream, at mid-height (h/2)
- saves the data in case/postProcessing/probe.csv
It takes two positional arguments: the taxon name (e.g. "Gogia_spiralis") and the case name (e.g. "Re500").
'''
# trace generated using paraview version 5.13.2
#import paraview
#paraview.compatibility.major = 5
#paraview.compatibility.minor = 13


#### import the simple module from the paraview
from paraview.simple import *
import sys
import parameters as par
import time
start = time.time()
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()
name = sys.argv[1]
taxon = getattr(par, name)
Re = str(sys.argv[2])
# create a new 'Open FOAM Reader'
print(f"Reading case.foam for {taxon.name} at {Re}")
casefoam = OpenFOAMReader(registrationName='case.foam', FileName=f'/mnt/shared/projects/nhm/jmcdermo/spirals/{taxon.name}/{Re}/case.foam')

# create a new 'Extract Time Steps'
print("Extracting time steps for time range: ", taxon.cfd[Re]["time_range"])
extractTimeSteps1 = ExtractTimeSteps(registrationName='ExtractTimeSteps1', Input=casefoam)
# Properties modified on extractTimeSteps1
extractTimeSteps1.SelectionMode = 'Select Time Range'
extractTimeSteps1.TimeStepRange = taxon.cfd[Re]["time_range"]
#extractTimeSteps1.TimeStepRange = [108, 364]


# create a new 'Probe Location'
probeLocation1 = ProbeLocation(registrationName='ProbeLocation1', Input=extractTimeSteps1,
    ProbeType='Fixed Radius Point Source')
probeLocation1.ProbeType.Center = [5*taxon.L, 0.0, taxon.h/2]


# create a new 'Plot Data Over Time'
plotDataOverTime1 = PlotDataOverTime(registrationName='PlotDataOverTime1', Input=probeLocation1)

UpdatePipeline(time=0.5, proxy=plotDataOverTime1)

# save data
SaveData(f'/mnt/shared/projects/nhm/jmcdermo/spirals/{taxon.name}/{Re}/postProcessing/probe.csv', proxy=plotDataOverTime1, RowDataArrays=['N', 'Time', 'avg(U (0))', 'avg(U (1))', 'avg(U (2))', 'avg(U (Magnitude))'])
end = time.time()
elapsed = end - start
print(f"Probe data saved to /mnt/shared/projects/nhm/jmcdermo/spirals/{taxon.name}/{Re}/postProcessing/probe.csv     (runtime = {elapsed} seconds)")