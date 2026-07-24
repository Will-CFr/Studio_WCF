import clr
# codigo para obtener el nombre de los links en revit en texto
clr.AddReference("RevitAPI")
from Autodesk.Revit.DB import *

clr.AddReference("RevitServices") # Referencia a la librería API de Revit 
from RevitServices.Persistence import DocumentManager # Importar el DocumentManager para acceder al documento actual

doc = DocumentManager.Instance.CurrentDBDocument # Obtener el documento actual  

links = FilteredElementCollector(doc).OfClass(RevitLinkInstance) # Obtener todas las instancias de enlaces en el documento

names = [link.Name for link in links] # Obtener los nombres de los enlaces

OUT = "\n".join(names) # Unir los nombres en una cadena de texto separada por saltos de línea"