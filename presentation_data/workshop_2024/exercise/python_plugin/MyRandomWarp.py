from paraview.util.vtkAlgorithm import *
from vtkmodules.numpy_interface import dataset_adapter as dsa
from vtkmodules.vtkCommonDataModel import vtkDataSet
import numpy as np

# TODO: define the name and label of this filter, as well as its accepted input type (vtkPointSet)
# We ideally want to specify that we only accept inputs that have a vector field attached to the points.
# "Simple" decorators does not support that but it is possible to inject some XML. See below :
# <InputArrayDomain attribute_type="point" name="input_normal" number_of_components="3" />
class RandomWarp(VTKPythonAlgorithmBase):
    def __init__(self):
        super().__init__(nInputPorts=1, nOutputPorts=1, outputType="vtkPointSet")
        self.WarpFactor = 1.0
        self.NormalArray = ""

    # Here we implemented a RequestDataObject that returns an instance of the input data type
    def RequestDataObject(self, request, inInfo, outInfo):
        inData = self.GetInputData(inInfo, 0, 0)
        outData = self.GetOutputData(outInfo, 0)
        assert inData is not None
        if outData is None or (not outData.IsA(inData.GetClassName())):
            outData = inData.NewInstance()
            outInfo.GetInformationObject(0).Set(outData.DATA_OBJECT(), outData)
        return super().RequestDataObject(request, inInfo, outInfo)

    # TODO: add the right decorators for this property. You can also add a range to have a slider in the UI
    def SetFactor(self, i):
        if i != self.WarpFactor:
            self.WarpFactor = i
            self.Modified()

    # TODO: add the right decorators for this property
    # Its domain is related to the available arrays in the input, but this domain is not supported by "simple" decorators.
    # Here is the xml to inject for it to work
    #
    # <ArrayListDomain attribute_type="Vectors" name="array_list">
    #     <RequiredProperties>
    #         <Property function="Input" name="Input" />
    #     </RequiredProperties>
    # </ArrayListDomain>
    def SetNormalArray(self, name):
        if name != self.NormalArray:
            self.NormalArray = name
            self.Modified()

    # Main logic
    def RequestData(self, request, inInfo, outInfo):
        # Retrieve input and output
        input = dsa.WrapDataObject(vtkDataSet.GetData(inInfo[0]))
        output = dsa.WrapDataObject(self.GetOutputData(outInfo, 0))

        # Output is mainly the same as the input so shallow copy overything
        output.ShallowCopy(input.VTKObject)

        # However points will be modified so we need to deep copy these
        output.Points.DeepCopy(input.Points.VTKObject)

        # TODO: Warp points according to the specified normal array. You can use `np.random.random_sample(np.shape(output.Points)[0])` to generate some
        # random factors for each point.
        # output.Points = [...]

        return 1
