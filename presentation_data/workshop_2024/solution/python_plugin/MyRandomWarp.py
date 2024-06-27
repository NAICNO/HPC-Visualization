from paraview.util.vtkAlgorithm import *
from vtkmodules.numpy_interface import dataset_adapter as dsa
from vtkmodules.vtkCommonDataModel import vtkDataSet
import numpy as np

@smproxy.filter(name="MyRandomWarp", label="My Random Warp")
@smproperty.input(name="Input", port_index=0)
@smdomain.datatype(dataTypes=["vtkPointSet"])
@smdomain.xml("""<InputArrayDomain attribute_type="point" name="input_normal" number_of_components="3" />""")
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

    @smproperty.stringvector(name="Normal")
    @smdomain.xml(\
        """<ArrayListDomain attribute_type="Vectors" name="array_list">
                <RequiredProperties>
                    <Property function="Input" name="Input" />
                </RequiredProperties>
            </ArrayListDomain>
        """)
    def SetNormalArray(self, name):
        if name != self.NormalArray:
            self.NormalArray = name
            self.Modified()


    @smproperty.doublevector(name="Factor", default_values="1")
    @smdomain.doublerange(min=0, max=10)
    def SetFactor(self, i):
        if i != self.WarpFactor:
            self.WarpFactor = i
            self.Modified()

    def RequestData(self, request, inInfo, outInfo):
        # Retrieve input and output
        input = dsa.WrapDataObject(vtkDataSet.GetData(inInfo[0]))
        output = dsa.WrapDataObject(self.GetOutputData(outInfo, 0))

        # Output is mainly the same as the input so shallow copy overything
        output.ShallowCopy(input.VTKObject)

        # However points will be modified so we need to deep copy these ones
        output.Points.DeepCopy(input.Points.VTKObject)

        # Warp points according to the specified normal array
        output.Points = output.Points + output.PointData[self.NormalArray] * np.random.random_sample(np.shape(output.Points)[0]) * self.WarpFactor

        return 1
