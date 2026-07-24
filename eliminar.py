import clr
clr.AddReference("RevitServices")
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

clr.AddReference("RevitAPI")
from Autodesk.Revit.DB import *

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)

doc = DocumentManager.Instance.CurrentDBDocument

# Entradas
filtered = IN[0]   # elementos MINIMO
all_elements = IN[1]
value_to_set = IN[2]

# asegurar listas
if not isinstance(filtered, list):
    filtered = [filtered]

if not isinstance(all_elements, list):
    all_elements = [all_elements]

# unwrap
filtered = [UnwrapElement(e) for e in filtered if e]
all_elements = [UnwrapElement(e) for e in all_elements if e]

# 🔥 función para obtener bounding box
def get_bbox(e):
    try:
        return e.get_BoundingBox(None)
    except:
        return None

# 🔥 función de intersección rápida (bounding box)
def intersects(bb1, bb2):
    if not bb1 or not bb2:
        return False
    
    return not (
        bb1.Max.X < bb2.Min.X or
        bb1.Min.X > bb2.Max.X or
        bb1.Max.Y < bb2.Min.Y or
        bb1.Min.Y > bb2.Max.Y or
        bb1.Max.Z < bb2.Min.Z or
        bb1.Min.Z > bb2.Max.Z
    )

# preparar bounding boxes de filtrados
filtered_bboxes = [(e, get_bbox(e)) for e in filtered]

result = []

TransactionManager.Instance.EnsureInTransaction(doc)

for e in all_elements:
    bb_e = get_bbox(e)
    
    if not bb_e:
        continue
    
    for f, bb_f in filtered_bboxes:
        if intersects(bb_e, bb_f):
            
            try:
                p = e.LookupParameter("Comments")
                if p and not p.IsReadOnly:
                    p.Set(value_to_set)
                    result.append(e)
            except:
                pass
            
            break  # ya intersectó con uno, no seguir

TransactionManager.Instance.TransactionTaskDone()

OUT = result