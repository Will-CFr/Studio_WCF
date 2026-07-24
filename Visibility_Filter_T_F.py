#Tenemos con IN0 el elementID del filtro y como IN1 el boolean para activar la visibilidad del filtro

#importamos el puente de Revit para acceder a las librerías de Revit y poder manipular los elementos de Revit desde Python
import clr
clr.AddReference('RevitAPI') #AddReference es el métedo para importar la librería de RevitAPI y acceder a sus clases
from Autodesk.Revit.DB import * #Namespace para acceder a las clases de Revit

