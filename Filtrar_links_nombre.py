import sys
import clr

clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *
from Autodesk.Revit.DB.Structure import *

clr.AddReference('RevitAPIUI')
from Autodesk.Revit.UI import *

clr.AddReference('System')
from System.Collections.Generic import List

clr.AddReference('RevitNodes')
import Revit
clr.ImportExtensions(Revit.GeometryConversion)
clr.ImportExtensions(Revit.Elements)

clr.AddReference('RevitServices')
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

doc = DocumentManager.Instance.CurrentDBDocument
uiapp = DocumentManager.Instance.CurrentUIApplication
uidoc = DocumentManager.Instance.CurrentUIApplication.ActiveUIDocument

# The inputs to this node will be stored as a list in the IN variables.
dataEnteringNode = IN

# Place your code below this line
links = UnwrapElement(IN[0])
filtros = IN[1]
salida = [[] for i in range(len(filtros))]
lista_sin_workset = []

for link_i in links:
	link_tipo_i = doc.GetElement(link_i.GetTypeId())
	#NOMBRE DE TIPO DEL LINK
	x = link_tipo_i.LookupParameter('Type Name').AsString()
	encontrado = False
	j=0
	for f_i in filtros:
		for str_i in f_i:
			#Lista de strings separados de filtro
			y = str_i.Split("*")
			if x.startswith(y[0]):
				encontrado = True
				break
		if encontrado:
			salida[j].append(link_i)
			#salida[j].append(link_tipo_i)
			break
		j+=1
	if encontrado == False:
		lista_sin_workset.append(link_i)
		#lista_sin_workset.append(link_tipo_i)		

# Assign your output to the OUT variable.
OUT = salida,lista_sin_workset