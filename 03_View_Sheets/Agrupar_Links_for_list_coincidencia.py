#Vamos a agrupar los links por su coincidencia según una lista de nombres
# importamos el puente entre python y Revit para acceder a las librerías de Revit y poder manipular los elementos de Revit desde Python
import clr
clr.AddReference('RevotAPI') #AddReference es el método para importar la librería de RevitAPI y acceder a sus clases
from Autodesk.Revit.DB import *

#importamos la librería de RevitNodes para acceder a la clase ElementSelector y UnwapElement
#RevitNodes viene del dynamoRevit que es el plugin que conecta Revit con Dynamo
clr.AddReference('RevitNodes')
import Revit
from Revit.Elements import * #Namespace para acceder a las clases de RevitNodes

