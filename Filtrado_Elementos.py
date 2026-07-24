# Load the Python Standard and DesignScript Libraries
import sys
import clr
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *

# The inputs to this node will be stored as a list in the IN variables.
dataEnteringNode = IN

# Place your code below this line
elementos_todos = IN[0]
elementos_filtro = IN[1]
ids_1 = [ele_1.Id for ele_1 in elementos_todos]
ids_2 = [ele_2.Id for ele_2 in elementos_filtro]
salida=[]
for id in ids_1:
	if id not in ids_2:
		salida.append(True)
	else:
		salida.append(False)
		
# Assign your output to the OUT variable.
OUT = salida