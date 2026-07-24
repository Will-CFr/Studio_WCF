# Con una lista de enteros, convertir a elementid

import clr

clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference('RevitServices')
from RevitServices.Persistence import DocumentManager

# Obtener el documento activo

doc = DocumentManager.Instance.CurrentDBDocument # esto es para obtener el documento activo

# Entrada solo funciona con dynamo

Ids = IN[0] # esto es para obtener la lista de enteros que se ingresa en dynamo

if not isinstance(Ids, list):
    Ids = [Ids] # si no es una lista, convertirlo en una lista

# Obtener los elementos 
# Crear una lista vacía para almacenar los elementos

elements = []

for wc in Ids: #wc es el iterativo para cada id en la lista de ids

    elwc = doc.GetElement(ElementId(wc)) # esto es para obtener el elemento a partir del id declaramos elwc para almacenar el elemento obtenido a partir del id
    #si es none filtrarlo
    if elwc is not None:
        elements.append(elwc) # esto es para agregar el elemento a la lista de elementos
    
OUT = elements # esto es para devolver la lista de elementos a dynamo
    




