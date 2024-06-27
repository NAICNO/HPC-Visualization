import numpy as np
import vtk
from vtk.util.numpy_support import numpy_to_vtk

filename = 'C:/pv/workshop_2024/exercise/custom_dataset/freiburgCampus360_3D/scan_001_points.dat'

data = np.loadtxt(filename) # load file
points = data[:, -3:]

vtkPoints = vtk.vtkPoints()
vtkPoints.SetData(numpy_to_vtk(points))

output = self.GetOutput()
output.SetPoints(vtkPoints)

vertices = vtk.vtkCellArray() # vtkCellArray to store vertices
num_points = vtkPoints.GetNumberOfPoints()

for i in range(num_points):
    vertices.InsertNextCell(1)
    vertices.InsertCellPoint(i)

output.SetVerts(vertices) # setting output
