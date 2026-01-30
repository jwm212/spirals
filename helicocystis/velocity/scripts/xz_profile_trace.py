# trace generated using paraview version 5.13.2
#import paraview
#paraview.compatibility.major = 5
#paraview.compatibility.minor = 13

#### import the simple module from the paraview
from paraview.simple import *
import numpy as np
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

cases = np.array(["v0.05", "v0.1", "v0.2", "v0.3", "v0.4", "v0.5"])
velocity = np.array([0.05, 0.1, 0.2, 0.3, 0.4, 0.5])
arr = np.arange(0,len(cases),1)

for i in arr:
    # find source
    #v01_40000vtk = FindSource('../v0.1/VTK/v0.1_40000.vtk')
    vtk = LegacyVTKReader(registrationName= cases[i]+'_40000.vtk', FileNames=['../'+cases[i]+'/VTK/'+cases[i]+'_40000.vtk'])
    #v01_40000vtk = LegacyVTKReader(registrationName= 'v0.1_40000.vtk', FileNames=['../v0.1/VTK/v0.1_40000.vtk'])
    # create a new 'Slice'
    slice1 = Slice(registrationName='Slice1', Input=vtk)

    # get active view
    renderView1 = GetActiveViewOrCreate('RenderView')
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [0.05297104298697119, -1.1875417892227726, 0.25635214438223297]
    renderView1.CameraFocalPoint = [0.10000000149011617, -6.786768581356654e-18, 0.059999998658895486]
    renderView1.CameraViewUp = [-0.09215148410865048, 0.16598564335199903, 0.9818130525602092]
    renderView1.CameraParallelScale = 0.3117691491478013
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [0.05297104298697119, -1.1875417892227726, 0.25635214438223297]
    renderView1.CameraFocalPoint = [0.10000000149011617, -6.786768581356654e-18, 0.059999998658895486]
    renderView1.CameraViewUp = [-0.09215148410865048, 0.16598564335199903, 0.9818130525602092]
    renderView1.CameraParallelScale = 0.3117691491478013

    # Properties modified on slice1.SliceType
    slice1.SliceType.Normal = [0.0, 1.0, 0.0]

    # show data in view
    slice1Display = Show(slice1, renderView1, 'GeometryRepresentation')

    # trace defaults for the display properties.
    slice1Display.Representation = 'Surface'

    # hide data in view
    Hide(vtk, renderView1)

    # update the view to ensure updated data information
    renderView1.Update()
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [0.05297104298697119, -1.1875417892227726, 0.25635214438223297]
    renderView1.CameraFocalPoint = [0.10000000149011617, -6.786768581356654e-18, 0.059999998658895486]
    renderView1.CameraViewUp = [-0.09215148410865048, 0.16598564335199903, 0.9818130525602092]
    renderView1.CameraParallelScale = 0.3117691491478013
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [0.05297104298697119, -1.1875417892227726, 0.25635214438223297]
    renderView1.CameraFocalPoint = [0.10000000149011617, -6.786768581356654e-18, 0.059999998658895486]
    renderView1.CameraViewUp = [-0.09215148410865048, 0.16598564335199903, 0.9818130525602092]
    renderView1.CameraParallelScale = 0.3117691491478013

    # create a new 'Clip'
    clip1 = Clip(registrationName='Clip1', Input=slice1)
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [0.05297104298697119, -1.1875417892227726, 0.25635214438223297]
    renderView1.CameraFocalPoint = [0.10000000149011617, -6.786768581356654e-18, 0.059999998658895486]
    renderView1.CameraViewUp = [-0.09215148410865048, 0.16598564335199903, 0.9818130525602092]
    renderView1.CameraParallelScale = 0.3117691491478013
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [0.05297104298697119, -1.1875417892227726, 0.25635214438223297]
    renderView1.CameraFocalPoint = [0.10000000149011617, -6.786768581356654e-18, 0.059999998658895486]
    renderView1.CameraViewUp = [-0.09215148410865048, 0.16598564335199903, 0.9818130525602092]
    renderView1.CameraParallelScale = 0.3117691491478013
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [0.05297104298697119, -1.1875417892227726, 0.25635214438223297]
    renderView1.CameraFocalPoint = [0.10000000149011617, -6.786768581356654e-18, 0.059999998658895486]
    renderView1.CameraViewUp = [-0.09215148410865048, 0.16598564335199903, 0.9818130525602092]
    renderView1.CameraParallelScale = 0.3117691491478013
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [0.05544577774341116, -1.1999237735861081, 0.1560169135628667]
    renderView1.CameraFocalPoint = [0.10000000149011616, -6.301367048146756e-18, 0.059999998658895465]
    renderView1.CameraViewUp = [-0.09466299086083314, 0.08289809233962266, 0.9920518254848046]
    renderView1.CameraParallelScale = 0.3117691491478013

    # Properties modified on clip1.ClipType
    clip1.ClipType.Origin = [0.10000000149011612, 0.0, 0.01574]
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

    # current camera placement for renderView1
    renderView1.CameraPosition = [0.05544577774341116, -1.1999237735861081, 0.1560169135628667]
    renderView1.CameraFocalPoint = [0.10000000149011616, -6.301367048146756e-18, 0.059999998658895465]
    renderView1.CameraViewUp = [-0.09466299086083314, 0.08289809233962266, 0.9920518254848046]
    renderView1.CameraParallelScale = 0.3117691491478013
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [0.05544577774341116, -1.1999237735861081, 0.1560169135628667]
    renderView1.CameraFocalPoint = [0.10000000149011616, -6.301367048146756e-18, 0.059999998658895465]
    renderView1.CameraViewUp = [-0.09466299086083314, 0.08289809233962266, 0.9920518254848046]
    renderView1.CameraParallelScale = 0.3117691491478013

    # create a new 'Clip'
    clip2 = Clip(registrationName='Clip2', Input=clip1)
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [0.05544577774341116, -1.1999237735861081, 0.1560169135628667]
    renderView1.CameraFocalPoint = [0.10000000149011616, -6.301367048146756e-18, 0.059999998658895465]
    renderView1.CameraViewUp = [-0.09466299086083314, 0.08289809233962266, 0.9920518254848046]
    renderView1.CameraParallelScale = 0.3117691491478013
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [0.05544577774341116, -1.1999237735861081, 0.1560169135628667]
    renderView1.CameraFocalPoint = [0.10000000149011616, -6.301367048146756e-18, 0.059999998658895465]
    renderView1.CameraViewUp = [-0.09466299086083314, 0.08289809233962266, 0.9920518254848046]
    renderView1.CameraParallelScale = 0.3117691491478013

    # Properties modified on clip2.ClipType
    clip2.ClipType.Origin = [0.0313, 0.0, 0.023499999195337296]

    # show data in view
    clip2Display = Show(clip2, renderView1, 'UnstructuredGridRepresentation')

    # trace defaults for the display properties.
    clip2Display.Representation = 'Surface'

    # hide data in view
    Hide(clip1, renderView1)

    # update the view to ensure updated data information
    renderView1.Update()
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [0.05544577774341116, -1.1999237735861081, 0.1560169135628667]
    renderView1.CameraFocalPoint = [0.10000000149011616, -6.301367048146756e-18, 0.059999998658895465]
    renderView1.CameraViewUp = [-0.09466299086083314, 0.08289809233962266, 0.9920518254848046]
    renderView1.CameraParallelScale = 0.3117691491478013
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [0.05544577774341116, -1.1999237735861081, 0.1560169135628667]
    renderView1.CameraFocalPoint = [0.10000000149011616, -6.301367048146756e-18, 0.059999998658895465]
    renderView1.CameraViewUp = [-0.09466299086083314, 0.08289809233962266, 0.9920518254848046]
    renderView1.CameraParallelScale = 0.3117691491478013

    # create a new 'Clip'
    clip3 = Clip(registrationName='Clip3', Input=clip2)
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [0.05544577774341116, -1.1999237735861081, 0.1560169135628667]
    renderView1.CameraFocalPoint = [0.10000000149011616, -6.301367048146756e-18, 0.059999998658895465]
    renderView1.CameraViewUp = [-0.09466299086083314, 0.08289809233962266, 0.9920518254848046]
    renderView1.CameraParallelScale = 0.3117691491478013

    # Properties modified on clip3
    clip3.Invert = 0

    # Properties modified on clip3.ClipType
    clip3.ClipType.Origin = [-0.0117, 0.0, 0.023499999195337296]

    # show data in view
    clip3Display = Show(clip3, renderView1, 'UnstructuredGridRepresentation')

    # trace defaults for the display properties.
    clip3Display.Representation = 'Surface'

    # hide data in view
    Hide(clip2, renderView1)

    # update the view to ensure updated data information
    renderView1.Update()
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [0.05544577774341116, -1.1999237735861081, 0.1560169135628667]
    renderView1.CameraFocalPoint = [0.10000000149011616, -6.301367048146756e-18, 0.059999998658895465]
    renderView1.CameraViewUp = [-0.09466299086083314, 0.08289809233962266, 0.9920518254848046]
    renderView1.CameraParallelScale = 0.3117691491478013
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [0.05544577774341116, -1.1999237735861081, 0.1560169135628667]
    renderView1.CameraFocalPoint = [0.10000000149011616, -6.301367048146756e-18, 0.059999998658895465]
    renderView1.CameraViewUp = [-0.09466299086083314, 0.08289809233962266, 0.9920518254848046]
    renderView1.CameraParallelScale = 0.3117691491478013

    # create a new 'Calculator'
    calculator1 = Calculator(registrationName='Calculator1', Input=clip3)
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [0.05544577774341116, -1.1999237735861081, 0.1560169135628667]
    renderView1.CameraFocalPoint = [0.10000000149011616, -6.301367048146756e-18, 0.059999998658895465]
    renderView1.CameraViewUp = [-0.09466299086083314, 0.08289809233962266, 0.9920518254848046]
    renderView1.CameraParallelScale = 0.3117691491478013

    # Properties modified on calculator1
    calculator1.Function = 'U_X*iHat + U_Z*kHat'

    # show data in view
    calculator1Display = Show(calculator1, renderView1, 'UnstructuredGridRepresentation')

    # trace defaults for the display properties.
    calculator1Display.Representation = 'Surface'

    # hide data in view
    Hide(clip3, renderView1)

    # update the view to ensure updated data information
    renderView1.Update()
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [0.05544577774341116, -1.1999237735861081, 0.1560169135628667]
    renderView1.CameraFocalPoint = [0.10000000149011616, -6.301367048146756e-18, 0.059999998658895465]
    renderView1.CameraViewUp = [-0.09466299086083314, 0.08289809233962266, 0.9920518254848046]
    renderView1.CameraParallelScale = 0.3117691491478013
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [0.05544577774341116, -1.1999237735861081, 0.1560169135628667]
    renderView1.CameraFocalPoint = [0.10000000149011616, -6.301367048146756e-18, 0.059999998658895465]
    renderView1.CameraViewUp = [-0.09466299086083314, 0.08289809233962266, 0.9920518254848046]
    renderView1.CameraParallelScale = 0.3117691491478013

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
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [0.05544577774341116, -1.1999237735861081, 0.1560169135628667]
    renderView1.CameraFocalPoint = [0.10000000149011616, -6.301367048146756e-18, 0.059999998658895465]
    renderView1.CameraViewUp = [-0.09466299086083314, 0.08289809233962266, 0.9920518254848046]
    renderView1.CameraParallelScale = 0.3117691491478013

    # create a new 'Resample To Image'
    resampleToImage1 = ResampleToImage(registrationName='ResampleToImage1', Input=calculator1)
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [0.05544577774341116, -1.1999237735861081, 0.1560169135628667]
    renderView1.CameraFocalPoint = [0.10000000149011616, -6.301367048146756e-18, 0.059999998658895465]
    renderView1.CameraViewUp = [-0.09466299086083314, 0.08289809233962266, 0.9920518254848046]
    renderView1.CameraParallelScale = 0.3117691491478013

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
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [0.05544577774341116, -1.1999237735861081, 0.1560169135628667]
    renderView1.CameraFocalPoint = [0.10000000149011616, -6.301367048146756e-18, 0.059999998658895465]
    renderView1.CameraViewUp = [-0.09466299086083314, 0.08289809233962266, 0.9920518254848046]
    renderView1.CameraParallelScale = 0.3117691491478013
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [0.05544577774341116, -1.1999237735861081, 0.1560169135628667]
    renderView1.CameraFocalPoint = [0.10000000149011616, -6.301367048146756e-18, 0.059999998658895465]
    renderView1.CameraViewUp = [-0.09466299086083314, 0.08289809233962266, 0.9920518254848046]
    renderView1.CameraParallelScale = 0.3117691491478013

    # create a new 'Glyph'
    glyph1 = Glyph(registrationName='Glyph1', Input=resampleToImage1,
        GlyphType='Arrow')
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [0.05544577774341116, -1.1999237735861081, 0.1560169135628667]
    renderView1.CameraFocalPoint = [0.10000000149011616, -6.301367048146756e-18, 0.059999998658895465]
    renderView1.CameraViewUp = [-0.09466299086083314, 0.08289809233962266, 0.9920518254848046]
    renderView1.CameraParallelScale = 0.3117691491478013

    # Properties modified on glyph1
    glyph1.GlyphType = '2D Glyph'
    glyph1.ScaleArray = ['POINTS', 'Result']
    #glyph1.ScaleFactor = 0.0056
    glyph1.ScaleFactor = 0.0017/velocity[i]
    glyph1.GlyphMode = 'All Points'


    # show data in view
    glyph1Display = Show(glyph1, renderView1, 'GeometryRepresentation')

    # trace defaults for the display properties.
    glyph1Display.Representation = 'Surface'
    glyph1Display.LineWidth = 5

    # show color bar/color legend
    glyph1Display.SetScalarBarVisibility(renderView1, True)

    # update the view to ensure updated data information
    renderView1.Update()
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [0.05544577774341116, -1.1999237735861081, 0.1560169135628667]
    renderView1.CameraFocalPoint = [0.10000000149011616, -6.301367048146756e-18, 0.059999998658895465]
    renderView1.CameraViewUp = [-0.09466299086083314, 0.08289809233962266, 0.9920518254848046]
    renderView1.CameraParallelScale = 0.3117691491478013
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [0.05544577774341116, -1.1999237735861081, 0.1560169135628667]
    renderView1.CameraFocalPoint = [0.10000000149011616, -6.301367048146756e-18, 0.059999998658895465]
    renderView1.CameraViewUp = [-0.09466299086083314, 0.08289809233962266, 0.9920518254848046]
    renderView1.CameraParallelScale = 0.3117691491478013

    # turn off scalar coloring
    ColorBy(glyph1Display, None)

    # Hide the scalar bar for this color map if no visible data is colored by it.
    HideScalarBarIfNotNeeded(resultLUT, renderView1)
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [0.05544577774341116, -1.1999237735861081, 0.1560169135628667]
    renderView1.CameraFocalPoint = [0.10000000149011616, -6.301367048146756e-18, 0.059999998658895465]
    renderView1.CameraViewUp = [-0.09466299086083314, 0.08289809233962266, 0.9920518254848046]
    renderView1.CameraParallelScale = 0.3117691491478013

    # Properties modified on glyph1.GlyphTransform
    glyph1.GlyphTransform.Rotate = [90.0, 0.0, 0.0]

    # update the view to ensure updated data information
    renderView1.Update()
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [0.05544577774341116, -1.1999237735861081, 0.1560169135628667]
    renderView1.CameraFocalPoint = [0.10000000149011616, -6.301367048146756e-18, 0.059999998658895465]
    renderView1.CameraViewUp = [-0.09466299086083314, 0.08289809233962266, 0.9920518254848046]
    renderView1.CameraParallelScale = 0.3117691491478013
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [0.05544577774341116, -1.1999237735861081, 0.1560169135628667]
    renderView1.CameraFocalPoint = [0.10000000149011616, -6.301367048146756e-18, 0.059999998658895465]
    renderView1.CameraViewUp = [-0.09466299086083314, 0.08289809233962266, 0.9920518254848046]
    renderView1.CameraParallelScale = 0.3117691491478013

    renderView1.ResetActiveCameraToPositiveY()

    # reset view to fit data
    renderView1.ResetCamera(False, 0.9)
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [0.029499761760234833, -0.2776180307606606, 0.022517368430271745]
    renderView1.CameraFocalPoint = [0.029499761760234833, 0.0, 0.022517368430271745]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 0.07185283362471641
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [0.029499761760234833, -0.2776180307606606, 0.022517368430271745]
    renderView1.CameraFocalPoint = [0.029499761760234833, 0.0, 0.022517368430271745]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 0.07185283362471641

    # hide data in view
    Hide(resampleToImage1, renderView1)
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [0.029499761760234833, -0.2776180307606606, 0.022517368430271745]
    renderView1.CameraFocalPoint = [0.029499761760234833, 0.0, 0.022517368430271745]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 0.07185283362471641

    # set active source
    SetActiveSource(calculator1)

    # show data in view
    calculator1Display = Show(calculator1, renderView1, 'UnstructuredGridRepresentation')

    # show color bar/color legend
    calculator1Display.SetScalarBarVisibility(renderView1, True)
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [0.029499761760234833, -0.2776180307606606, 0.022517368430271745]
    renderView1.CameraFocalPoint = [0.029499761760234833, 0.0, 0.022517368430271745]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 0.07185283362471641
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [0.029499761760234833, -0.2776180307606606, 0.022517368430271745]
    renderView1.CameraFocalPoint = [0.029499761760234833, 0.0, 0.022517368430271745]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 0.07185283362471641
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [0.029499761760234833, -0.2776180307606606, 0.022517368430271745]
    renderView1.CameraFocalPoint = [0.029499761760234833, 0.0, 0.022517368430271745]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 0.07185283362471641

    LoadPalette(paletteName='WhiteBackground')
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [0.029499761760234833, -0.2776180307606606, 0.022517368430271745]
    renderView1.CameraFocalPoint = [0.029499761760234833, 0.0, 0.022517368430271745]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 0.07185283362471641
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [0.029499761760234833, -0.2776180307606606, 0.022517368430271745]
    renderView1.CameraFocalPoint = [0.029499761760234833, 0.0, 0.022517368430271745]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 0.07185283362471641
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [0.029499761760234833, -0.2776180307606606, 0.022517368430271745]
    renderView1.CameraFocalPoint = [0.029499761760234833, 0.0, 0.022517368430271745]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 0.07185283362471641

    # Rescale transfer function
    resultLUT.RescaleTransferFunction(0.0, velocity[i]+0.2*velocity[i])

    # Rescale transfer function
    resultPWF.RescaleTransferFunction(0.0, velocity[i]+0.2*velocity[i])

    # Rescale 2D transfer function
    resultTF2D.RescaleTransferFunction(0.0, velocity[i]+0.2*velocity[i], 0.0, 1.0)
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [0.029499761760234833, -0.2776180307606606, 0.022517368430271745]
    renderView1.CameraFocalPoint = [0.029499761760234833, 0.0, 0.022517368430271745]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 0.07185283362471641
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [0.029499761760234833, -0.2776180307606606, 0.022517368430271745]
    renderView1.CameraFocalPoint = [0.029499761760234833, 0.0, 0.022517368430271745]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 0.07185283362471641
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [0.029499761760234833, -0.2776180307606606, 0.022517368430271745]
    renderView1.CameraFocalPoint = [0.029499761760234833, 0.0, 0.022517368430271745]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 0.07185283362471641
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [0.029499761760234833, -0.2776180307606606, 0.022517368430271745]
    renderView1.CameraFocalPoint = [0.029499761760234833, 0.0, 0.022517368430271745]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 0.07185283362471641

    # hide color bar/color legend
    calculator1Display.SetScalarBarVisibility(renderView1, False)
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [0.029499761760234833, -0.2776180307606606, 0.022517368430271745]
    renderView1.CameraFocalPoint = [0.029499761760234833, 0.0, 0.022517368430271745]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 0.07185283362471641

    renderView1.ResetActiveCameraToPositiveY()

    # reset view to fit data
    renderView1.ResetCamera(False, 0.9)
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [0.029499761760234833, -0.2776180307606606, 0.022517368430271745]
    renderView1.CameraFocalPoint = [0.029499761760234833, 0.0, 0.022517368430271745]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 0.07185283362471641
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [0.029499761760234833, -0.22943638905839717, 0.022517368430271745]
    renderView1.CameraFocalPoint = [0.029499761760234833, 0.0, 0.022517368430271745]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 0.07185283362471641
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [0.029499761760234833, -0.18961685046148524, 0.022517368430271745]
    renderView1.CameraFocalPoint = [0.029499761760234833, 0.0, 0.022517368430271745]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 0.07185283362471641
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [0.029499761760234833, -0.1567081408772605, 0.022517368430271745]
    renderView1.CameraFocalPoint = [0.029499761760234833, 0.0, 0.022517368430271745]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 0.07185283362471641

    # Hide orientation axes
    renderView1.OrientationAxesVisibility = 0

    # get the material library
    materialLibrary1 = GetMaterialLibrary()
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [0.029499761760234833, -0.1567081408772605, 0.022517368430271745]
    renderView1.CameraFocalPoint = [0.029499761760234833, 0.0, 0.022517368430271745]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 0.07185283362471641
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [0.029499761760234833, -0.1567081408772605, 0.022517368430271745]
    renderView1.CameraFocalPoint = [0.029499761760234833, 0.0, 0.022517368430271745]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 0.07185283362471641
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [0.029499761760234833, -0.1567081408772605, 0.022517368430271745]
    renderView1.CameraFocalPoint = [0.029499761760234833, 0.0, 0.022517368430271745]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 0.07185283362471641

    # Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
    resultLUT.ApplyPreset('Turbo', True)
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [0.029499761760234833, -0.1567081408772605, 0.022517368430271745]
    renderView1.CameraFocalPoint = [0.029499761760234833, 0.0, 0.022517368430271745]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 0.07185283362471641
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [0.029499761760234833, -0.1567081408772605, 0.022517368430271745]
    renderView1.CameraFocalPoint = [0.029499761760234833, 0.0, 0.022517368430271745]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 0.07185283362471641

    # get layout
    layout1 = GetLayout()

    # layout/tab size in pixels
    layout1.SetSize(2152, 1350)

    # current camera placement for renderView1
    renderView1.CameraPosition = [0.029499761760234833, -0.1567081408772605, 0.022517368430271745]
    renderView1.CameraFocalPoint = [0.029499761760234833, 0.0, 0.022517368430271745]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 0.07185283362471641
    
    renderView1.ResetCamera(True, 0.9)
    # save screenshot
    SaveScreenshot(filename='../' + cases[i] + '/postProcessing/xz_profile.png', viewOrLayout=renderView1, location=16, ImageResolution=[3840, 2160])

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