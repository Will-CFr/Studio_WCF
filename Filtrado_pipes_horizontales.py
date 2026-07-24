import clr
clr.AddReference("RevitAPI")
from Autodesk.Revit.DB import *

# Entrada desde Dynamo
pipes = UnwrapElement(IN[0])

horizontales = []
verticales = []

tolerance = 0.001

for p in pipes:

    if p is None:
        continue

    loc = p.Location

    # validar curva
    if not hasattr(loc, "Curve"):
        continue

    try:
        curve = loc.Curve
    except:
        continue

    if curve is None:
        continue

    direction = curve.Direction

    # 🔥 HORIZONTAL
    if abs(direction.Z) < tolerance:
        horizontales.append(p)
    else:
        verticales.append(p)

# OUTPUT
OUT = horizontales, verticales