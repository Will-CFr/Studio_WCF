#Leer los filtros aplicados en la vista activa

#importamos el puente de Revit para acceder a las librerías de Revit y poder manipular los elementos de Revit desde Python
import clr

clr.AddReference('RevitAPI') # Importamos la librería de RevitAPI con el método AddReference para acceder a las clases de Revit
from Autodesk.Revit.DB import * #Namespace para acceder a las clases de Revit

#Importamos la librería de RevitServices para acceder a la clase DocumentManager
clr.AddReference('RevitServices')
from RevitServices.Persistence import DocumentManager #Namespace para acceder a la clase DocumentManager

#Obtenemos el documento activo
doc = DocumentManager.Instance.CurrentDBDocument

#Vista Activa
activeview = doc.ActiveView

#Obtenemoos los ids de los filtros aplicados en la vista activa
filterIds = activeview.GetFilters()

#Creamos una lista para almacenar los nombres de los filtros aplicados
filtersnames = []
ids = []
#Recorrer los filtros aplicados en la vista activa y obtener sus nombres

for i in filterIds:

    #Obtenemos el filtro por su id
    filter = doc.GetElement(i)
    #obtener los ids
    ids.append(filter) #filter.Id obtiene el id del filtro, pero queremos el elemento completo para obtener su nombre
    #Guardamos el nombre
    filtersnames.append(filter.Name)

OUT = ids, filtersnames # Devolvemos la lista de nombres de los filtros aplicados en la vista activa a Dynamo





