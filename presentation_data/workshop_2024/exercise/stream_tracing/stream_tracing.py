# trace generated using paraview version 5.12.1
#import paraview
#paraview.compatibility.major = 5
#paraview.compatibility.minor = 12

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# create a new 'Wavelet'
wavelet1 = Wavelet(registrationName='Wavelet1')

# Properties modified on wavelet1
wavelet1.WholeExtent = [-50, 50, -50, 50, -50, 50]

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')

# show data in view
wavelet1Display = Show(wavelet1, renderView1, 'UniformGridRepresentation')

# trace defaults for the display properties.
wavelet1Display.Representation = 'Outline'

# reset view to fit data
renderView1.ResetCamera(False, 0.9)

# get the material library
materialLibrary1 = GetMaterialLibrary()

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Random Vectors'
randomVectors1 = RandomVectors(registrationName='RandomVectors1', Input=wavelet1)

# show data in view
randomVectors1Display = Show(randomVectors1, renderView1, 'UniformGridRepresentation')

# trace defaults for the display properties.
randomVectors1Display.Representation = 'Outline'

# hide data in view
Hide(wavelet1, renderView1)

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Stream Tracer'
streamTracer1 = StreamTracer(registrationName='StreamTracer1', Input=randomVectors1,
    SeedType='Line')

# show data in view
streamTracer1Display = Show(streamTracer1, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
streamTracer1Display.Representation = 'Surface'

# show color bar/color legend
streamTracer1Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# get color transfer function/color map for 'RTData'
rTDataLUT = GetColorTransferFunction('RTData')

# get opacity transfer function/opacity map for 'RTData'
rTDataPWF = GetOpacityTransferFunction('RTData')

# get 2D transfer function for 'RTData'
rTDataTF2D = GetTransferFunction2D('RTData')

# toggle interactive widget visibility (only when running from the GUI)
ShowInteractiveWidgets(proxy=streamTracer1.SeedType)

# Properties modified on streamTracer1
streamTracer1.SeedType = 'Point Cloud'

# update the view to ensure updated data information
renderView1.Update()

# Rescale transfer function
rTDataLUT.RescaleTransferFunction(43.51658630371094, 285.4937744140625)

# Rescale transfer function
rTDataPWF.RescaleTransferFunction(43.51658630371094, 285.4937744140625)

# hide data in view
Hide(randomVectors1, renderView1)

#================================================================
# addendum: following script captures some of the application
# state to faithfully reproduce the visualization during playback
#================================================================

# get layout
layout1 = GetLayout()

#--------------------------------
# saving layout sizes for layouts

# layout/tab size in pixels
layout1.SetSize(2432, 1062)

#-----------------------------------
# saving camera placements for views

# current camera placement for renderView1
renderView1.CameraPosition = [0.0, 0.0, 334.60652149512316]
renderView1.CameraParallelScale = 86.60254037844386


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
# SaveScreenshot("path/to/screenshot.png")
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
## https://kitware.github.io/paraview-docs/latest/python/paraview.simple.html
##--------------------------------------------