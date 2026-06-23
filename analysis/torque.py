# trace generated using paraview version 5.13.2
#import paraview
#paraview.compatibility.major = 5
#paraview.compatibility.minor = 13

#### import the simple module from the paraview
from paraview.simple import *
import time
import sys
import parameters as par
start_time = time.time()
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()
name=sys.argv[1]
taxon = getattr(par, name)
Re=str(sys.argv[2])
# create a new 'Open FOAM Reader'
print(f"Reading case.foam for {taxon.name} at {Re}")
casefoam = OpenFOAMReader(registrationName='case.foam', FileName=f'/mnt/shared/projects/nhm/jmcdermo/spirals/{taxon.name}/{Re}/case.foam')

# Properties modified on casefoam
casefoam.MeshRegions = ['patch/HH']
casefoam.CellArrays = ['p']

# create a new 'Extract Time Steps'
print("Extracting time steps for time range: ", taxon.cfd[Re]["time_range"])
extractTimeSteps1 = ExtractTimeSteps(registrationName='ExtractTimeSteps1', Input=casefoam)
# Properties modified on extractTimeSteps1
extractTimeSteps1.SelectionMode = 'Select Time Range'
extractTimeSteps1.TimeStepRange = taxon.cfd[Re]["time_range"]


# create a new 'Generate Surface Normals'
print("Generating surface normals...")
generateSurfaceNormals1 = GenerateSurfaceNormals(registrationName='GenerateSurfaceNormals1', Input=extractTimeSteps1)

# create a new 'Calculator'
print("Calculating force...")
calculator1 = Calculator(registrationName='Calculator1', Input=generateSurfaceNormals1)

# Properties modified on calculator1
calculator1.ResultArrayName = 'Force'
calculator1.Function = '1025*p*Normals'

# create a new 'Calculator'
print("Calculating torque...")
calculator2 = Calculator(registrationName='Calculator2', Input=calculator1)

# Properties modified on calculator2
calculator2.ResultArrayName = 'Torque'
calculator2.Function = 'cross(coords,Force)'

# create a new 'Integrate Variables'
print("Integrating over area...")
integrateVariables1 = IntegrateVariables(registrationName='IntegrateVariables1', Input=calculator2)

# create a new 'Plot Data Over Time'
print("Plotting data over time...")
plotDataOverTime1 = PlotDataOverTime(registrationName='PlotDataOverTime1', Input=integrateVariables1)

UpdatePipeline(time=130.0, proxy=plotDataOverTime1)

# save data
print(f"Saving data to /mnt/shared/projects/nhm/jmcdermo/spirals/{taxon.name}/{Re}/postProcessing/torque.csv")
SaveData(f'/mnt/shared/projects/nhm/jmcdermo/spirals/{taxon.name}/{Re}/postProcessing/torque.csv', proxy=plotDataOverTime1, RowDataArrays=['N', 'Time', 'avg(Force (0))', 'avg(Force (1))', 'avg(Force (2))', 'avg(Force (Magnitude))', 'avg(Normals (0))', 'avg(Normals (1))', 'avg(Normals (2))', 'avg(Normals (Magnitude))', 'avg(Torque (0))', 'avg(Torque (1))', 'avg(Torque (2))', 'avg(Torque (Magnitude))', 'avg(X)', 'avg(Y)', 'avg(Z)', 'avg(p)', 'max(Force (0))', 'max(Force (1))', 'max(Force (2))', 'max(Force (Magnitude))', 'max(Normals (0))', 'max(Normals (1))', 'max(Normals (2))', 'max(Normals (Magnitude))', 'max(Torque (0))', 'max(Torque (1))', 'max(Torque (2))', 'max(Torque (Magnitude))', 'max(X)', 'max(Y)', 'max(Z)', 'max(p)', 'med(Force (0))', 'med(Force (1))', 'med(Force (2))', 'med(Force (Magnitude))', 'med(Normals (0))', 'med(Normals (1))', 'med(Normals (2))', 'med(Normals (Magnitude))', 'med(Torque (0))','sum(X)','sum(Y)','sum(Z)','sum(p)','vtkValidPointMask'],
    FieldAssociation='Row Data')
end_time = time.time()
print("Done.")
print(f"Total runtime: {end_time - start_time} seconds")