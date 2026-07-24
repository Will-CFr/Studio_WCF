import clr

# Revit API
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

# Entradas
elementos = UnwrapElement(IN[0])

# Asegurar lista
if not isinstance(elementos, list):
    elementos = [elementos]

viewports = []
resto = []

for elem in elementos:
    if isinstance(elem, Viewport):
        viewports.append(elem)
    else:
        resto.append(elem)

# Salidas
OUT = viewports, resto