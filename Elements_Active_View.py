#Obtenemos los elementos activos de la vista actual
#importamos la librería language common runtime
import clr
#importamos 'RevitApPI' con el método 'AddReference' para acceder a las clases de Revit
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import * #Namespace para acceder a las clases de Revit

#importamos RevitServices para acceder a la clase DocumentManager
clr.AddReference('RevitServices')
from RevitServices.Persistence import DocumentManager #Namespace para acceder a la clase DocumentManager

#Documento Actual
wcdoc = DocumentManager.Instance.CurrentDBDocument

#Vista activa
ActiveViewWC = wcdoc.ActiveView

#Recolección de elementos activos en la vista
Wccollector = FilteredElementCollector(wcdoc, ActiveViewWC.Id)

#Obtenemos los elementos activos en la vista actual
wcelements = Wccollector.WhereElementIsNotElementType().ToElements()

Out = wcelements #Devolvemos la lista de elementos activos en la vista actual a Dynamo
