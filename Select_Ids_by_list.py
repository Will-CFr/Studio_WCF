# Tengo como entrada una lista de elementos IN0 y quiero que se seleccionen en el modelo
# 
import clr

clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference('RevitServices')
from RevitServices.Persistence import DocumentManager

# importamos UI

clr.AddReference('RevitAPIUI')
from Autodesk.Revit.UI import *

# para usar list
from System.Collections.Generic import List

# obtener el documento activo

doc = DocumentManager.Instance.CurrentDBDocument

#obtenemos la aplicación activa

uidoc = DocumentManager.Instance.CurrentUIApplication.ActiveUIDocument

# Entrada solo funciona con dynamo

Ids = IN[0]

# si no es una lista 

if not isinstance(Ids, list):
    Ids = [Ids]

# codigo para seleccionar en el modelo

#obtener el elementid

elements = List[ElementId]()

for i in Ids:
    #elements.Add(i.Id) elements id
    elements.Add(ElementId(int(i)))

#seleccionar en Revit

uidoc.Selection.SetElementIds(elements)

OUT = Ids # esto es para devolver la lista de ids a dynamo
