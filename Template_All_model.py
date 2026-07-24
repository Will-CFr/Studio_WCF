#Vamos obtener los templates del modelo
#importamos el puente entre python y Revit para acceder a las librerías de Revit y poder manipular los elementos de Revit desde Python
import clr # common language runtime, es el puente entre python y .net framework

clr.AddReference('RevitAPI') #AddReference es el método para importar la librería de RevitAPI y acceder a sus clases
from Autodesk.Revit.DB import * #namespace para acceder a las clases DB de RevitAPI DB

clr.AddReference('RevitServices') #AddReference es el método para importar la librería de RevitServices y acceder a sus clases
from RevitServices.Persistence import DocumentManager #namespace para acceder a la clase DocumentManager de RevitServices

#ingresamos el documento activo de Revit
doc = DocumentManager.Instance.CurrentDBDocument #CurrentDBDocument es el documento activo de Revit

#los templates son views por eso accedemos a todas las vistas del documento activo y filtramos por las que son templates
views = FilteredElementCollector(doc).OfClass(View).ToElements() #FilteredElementCollector es el método para filtrar elementos del documento activo, OfClass es el método para filtrar por clase y ToElements es el método para convertir el resultado en una lista de elementos

#Filtramos solo las vistas que son templates
templates = []

for view in views:
    if view.IsTemplate:
        templates.append(view)

OUT = templates #Out es la variable de salida que se utiliza para enviar datos a Dynamo