import clr

clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *
from Autodesk.Revit.DB.Plumbing import Pipe

# Entrada: solo pipes
pipes = IN[0]

# Asegurar lista
if not isinstance(pipes, list):
    pipes = [pipes]

# Resultado
pipesOver2m = []

# 2 metros en pies
limit = 4 * 3.28084

for pipe in pipes:
    
    revitPipe = pipe.InternalElement
    
    # Longitud
    length = revitPipe.get_Parameter(
        BuiltInParameter.CURVE_ELEM_LENGTH
    ).AsDouble()
    
    # Filtrar
    if length > limit:
        pipesOver2m.append(pipe)

# Salida
OUT = pipesOver2m