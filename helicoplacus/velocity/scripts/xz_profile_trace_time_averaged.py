# trace generated using paraview version 5.13.2
#import paraview
#paraview.compatibility.major = 5
#paraview.compatibility.minor = 13

#### import the simple module from the paraview
from paraview.simple import *
import numpy as np
import glob
import os
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

cases = np.array(["v0.05", "v0.1", "v0.2", "v0.3", "v0.4", "v0.5"])
velocity = np.array([0.05, 0.1, 0.2, 0.3, 0.4, 0.5])
arr = np.arange(0,len(cases),1)

for i in arr:
    # find source
    #v01_40000vtk = FindSource('../v0.1/VTK/v0.1_40000.vtk')
    #vtk = LegacyVTKReader(registrationName= cases[i]+'_40000.vtk', FileNames=['../'+cases[i]+'/VTK/'+cases[i]+'_40000.vtk'])
    #v01_40000vtk = LegacyVTKReader(registrationName= 'v0.1_40000.vtk', FileNames=['../v0.1/VTK/v0.1_40000.vtk'])
    vtk_dir = os.path.join('..', cases[i], 'VTK')
    vtk_files = glob.glob(os.path.join(vtk_dir, '*.vtk'))
    if not vtk_files:
        raise FileNotFoundError(f'No .vtk files in {vtk_dir}')
    # sort by modification time (oldest->newest) and take last 10
    vtk_files_sorted = sorted(vtk_files, key=os.path.getmtime)
    last_files = vtk_files_sorted[-10:]
    print(f'Processing case {cases[i]} with velocity {velocity[i]} m/s using files: {last_files}')
    # if you prefer lexicographic order (useful when filenames are zero-padded timestamps) use:
    # last_files = sorted(vtk_files)[-10:]
    vtk = LegacyVTKReader(registrationName=f'{cases[i]}_last{len(last_files)}.vtk', FileNames=last_files)   
    # create a new 'Temporal Statistics'
    temporalStatistics1 = TemporalStatistics(registrationName='TemporalStatistics1', Input=vtk)

    # get active view
    renderView1 = GetActiveViewOrCreate('RenderView')

    # show data in view
    temporalStatistics1Display = Show(temporalStatistics1, renderView1, 'UnstructuredGridRepresentation')

    # trace defaults for the display properties.
    temporalStatistics1Display.Representation = 'Surface'

    # hide data in view
    Hide(vtk, renderView1)
    # update the view to ensure updated data information
    renderView1.Update()
   
    # create a new 'Slice'
    slice1 = Slice(registrationName='Slice1', Input=temporalStatistics1)

    # get active view
    renderView1 = GetActiveViewOrCreate('RenderView')
    

    # Properties modified on slice1.SliceType
    slice1.SliceType.Normal = [0.0, 1.0, 0.0]

    # show data in view
    slice1Display = Show(slice1, renderView1, 'GeometryRepresentation')

    # trace defaults for the display properties.
    slice1Display.Representation = 'Surface'

    # hide data in view
    Hide(temporalStatistics1, renderView1)

    # update the view to ensure updated data information
    renderView1.Update()
    # Adjust camera


    # create a new 'Clip'
    clip1 = Clip(registrationName='Clip1', Input=slice1)
    # Adjust camera


    # Properties modified on clip1.ClipType
    clip1.ClipType.Origin = [0.10000000149011612, 0.0, 0.047]
    clip1.ClipType.Normal = [0.0, 0.0, 1.0]

    # show data in view
    clip1Display = Show(clip1, renderView1, 'UnstructuredGridRepresentation')

    # trace defaults for the display properties.
    clip1Display.Representation = 'Surface'

    # hide data in view
    Hide(slice1, renderView1)

    # update the view to ensure updated data information
    renderView1.Update()
    # Adjust camera

    # create a new 'Clip'
    clip2 = Clip(registrationName='Clip2', Input=clip1)
    # Adjust camera


    # Properties modified on clip2.ClipType
    clip2.ClipType.Origin = [0.094, 0.0, 0.023499999195337296]

    # show data in view
    clip2Display = Show(clip2, renderView1, 'UnstructuredGridRepresentation')

    # trace defaults for the display properties.
    clip2Display.Representation = 'Surface'

    # hide data in view
    Hide(clip1, renderView1)

    # update the view to ensure updated data information
    renderView1.Update()
    # Adjust camera



    # create a new 'Clip'
    clip3 = Clip(registrationName='Clip3', Input=clip2)
    # Adjust camera


    # Properties modified on clip3
    clip3.Invert = 0

    # Properties modified on clip3.ClipType
    clip3.ClipType.Origin = [-0.035, 0.0, 0.023499999195337296]

    # show data in view
    clip3Display = Show(clip3, renderView1, 'UnstructuredGridRepresentation')

    # trace defaults for the display properties.
    clip3Display.Representation = 'Surface'

    # hide data in view
    Hide(clip2, renderView1)

    # update the view to ensure updated data information
    renderView1.Update()

    # create a new 'Calculator'
    calculator1 = Calculator(registrationName='Calculator1', Input=clip3)


    # Properties modified on calculator1
    calculator1.Function = 'U_average_X*iHat + U_average_Z*kHat'

    # show data in view
    calculator1Display = Show(calculator1, renderView1, 'UnstructuredGridRepresentation')

    # trace defaults for the display properties.
    calculator1Display.Representation = 'Surface'

    # hide data in view
    Hide(clip3, renderView1)

    # update the view to ensure updated data information
    renderView1.Update()

    # set scalar coloring
    ColorBy(calculator1Display, ('POINTS', 'Result', 'Magnitude'))

    # rescale color and/or opacity maps used to include current data range
    calculator1Display.RescaleTransferFunctionToDataRange(True, False)

    # show color bar/color legend
    calculator1Display.SetScalarBarVisibility(renderView1, True)

    # get 2D transfer function for 'Result'
    resultTF2D = GetTransferFunction2D('Result')

    # get color transfer function/color map for 'Result'
    resultLUT = GetColorTransferFunction('Result')
    resultLUT.TransferFunction2D = resultTF2D
    resultLUT.RGBPoints = [0.0, 0.231373, 0.298039, 0.752941, 0.060401074260587245, 0.865003, 0.865003, 0.865003, 0.12080214852117449, 0.705882, 0.0156863, 0.14902]
    resultLUT.ScalarRangeInitialized = 1.0

    # get opacity transfer function/opacity map for 'Result'
    resultPWF = GetOpacityTransferFunction('Result')
    resultPWF.Points = [0.0, 0.0, 0.5, 0.0, 0.12080214852117449, 1.0, 0.5, 0.0]
    resultPWF.ScalarRangeInitialized = 1

    # create a new 'Resample To Image'
    resampleToImage1 = ResampleToImage(registrationName='ResampleToImage1', Input=calculator1)

    # Properties modified on resampleToImage1
    resampleToImage1.SamplingDimensions = [20, 1, 10]

    # show data in view
    resampleToImage1Display = Show(resampleToImage1, renderView1, 'UniformGridRepresentation')

    # trace defaults for the display properties.
    resampleToImage1Display.Representation = 'Slice'

    # hide data in view
    Hide(calculator1, renderView1)

    # show color bar/color legend
    resampleToImage1Display.SetScalarBarVisibility(renderView1, True)

    # update the view to ensure updated data information
    renderView1.Update()

    # create a new 'Glyph'
    glyph1 = Glyph(registrationName='Glyph1', Input=resampleToImage1,
        GlyphType='Arrow')

    # Properties modified on glyph1
    glyph1.GlyphType = '2D Glyph'
    glyph1.ScaleArray = ['POINTS', 'Result']
    #glyph1.ScaleFactor = 0.0056
    glyph1.ScaleFactor = 0.005/velocity[i]
    glyph1.GlyphMode = 'All Points'


    # show data in view
    glyph1Display = Show(glyph1, renderView1, 'GeometryRepresentation')

    # trace defaults for the display properties.
    glyph1Display.Representation = 'Surface'
    glyph1Display.LineWidth = 5.0

    # show color bar/color legend
    glyph1Display.SetScalarBarVisibility(renderView1, True)

    # update the view to ensure updated data information
    renderView1.Update()

    # turn off scalar coloring
    ColorBy(glyph1Display, None)

    # Hide the scalar bar for this color map if no visible data is colored by it.
    HideScalarBarIfNotNeeded(resultLUT, renderView1)

    # Properties modified on glyph1.GlyphTransform
    glyph1.GlyphTransform.Rotate = [90.0, 0.0, 0.0]

    # update the view to ensure updated data information
    renderView1.Update()

    renderView1.ResetActiveCameraToPositiveY()

    # reset view to fit data
    renderView1.ResetCamera(False, 0.9)

    # hide data in view
    Hide(resampleToImage1, renderView1)

    # set active source
    SetActiveSource(calculator1)

    # show data in view
    calculator1Display = Show(calculator1, renderView1, 'UnstructuredGridRepresentation')

    # show color bar/color legend
    calculator1Display.SetScalarBarVisibility(renderView1, True)

    LoadPalette(paletteName='WhiteBackground')

    # Rescale transfer function
    resultLUT.RescaleTransferFunction(0.0, velocity[i]+0.2*velocity[i])

#### **** Getting consistent color bars **** ####
    # Rescale transfer function
    resultPWF.RescaleTransferFunction(0.0, velocity[i]+0.2*velocity[i])

    # Rescale 2D transfer function
    resultTF2D.RescaleTransferFunction(0.0, velocity[i]+0.2*velocity[i], 0.0, 1.0)

    # hide color bar/color legend
    calculator1Display.SetScalarBarVisibility(renderView1, False)

    renderView1.ResetActiveCameraToPositiveY()

    # reset view to fit data
    renderView1.ResetCamera(True, 1.0)

    # Hide orientation axes
    renderView1.OrientationAxesVisibility = 0

    # get the material library
    materialLibrary1 = GetMaterialLibrary()

    # Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
    resultLUT.ApplyPreset('Turbo', True)

    # get layout
    layout1 = GetLayout()

    # layout/tab size in pixels
    layout1.SetSize(2152, 1350)

    # current camera placement for renderView1
    renderView1.CameraPosition = [0.029499761760234833, -0.1567081408772605, 0.022517368430271745]
    renderView1.CameraFocalPoint = [0.029499761760234833, 0.0, 0.022517368430271745]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 0.07185283362471641

    # save screenshot
    SaveScreenshot(filename='../' + cases[i] + '/postProcessing/xz_profile_t_avrg.png', viewOrLayout=renderView1, location=16, ImageResolution=[3840, 2160])
    print('Saved screenshot for case ' + cases[i] + ' at velocity ' + str(velocity[i]) + ' m/s: ' + 'xz_profile_t_avrg.png')
    # remove pipeline objects so next iteration doesn't overlap them
    Delete(glyph1)
    Delete(resampleToImage1)
    Delete(calculator1)
    Delete(clip3)
    Delete(clip2)
    Delete(clip1)
    Delete(slice1)
    Delete(vtk)
    # remove python references
    del glyph1, resampleToImage1, calculator1, clip3, clip2, clip1, slice1, vtk

    # force a render/update
    renderView1.Update()


##--------------------------------------------
## You may need to add some code at the end of this python script depending on your usage, eg:
#
## Render all views to see them appears
# RenderAllViews()
#
## Interact with the view, usefull when running from pvpython
# Interact()
#
## Save a screenshot of the active view
#SaveScreenshot("../v0.1/postProcessing/xz_profile.png", ImageResolution=[3840, 2160])
#
## Save a screenshot of a layout (multiple splitted view)
# SaveScreenshot("path/to/screenshot.png", GetLayout())
#
## Save all "Extractors" from the pipeline browser
# SaveExtracts()
#
## Save a animation of the current active view
# SaveAnimation()
#
## Please refer to the documentation of paraview.simple
## https://www.paraview.org/paraview-docs/latest/python/paraview.simple.html
##--------------------------------------------