import clr

# Revit API
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

# Revit Services
clr.AddReference('RevitServices')
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

# Documento actual
doc = DocumentManager.Instance.CurrentDBDocument

# Entrada
viewports = UnwrapElement(IN[0])
separacion_cm = (IN[1])

# Separación en cm

# Convertir cm a pies
separacion = separacion_cm / 30.48

# Ordenar de izquierda a derecha
viewports = sorted(
    viewports,
    key=lambda vp: vp.GetBoxCenter().X
)

TransactionManager.Instance.EnsureInTransaction(doc)

# Primer viewport como referencia
vp_base = viewports[0]

base_center = vp_base.GetBoxCenter()

# Ancho del primero
base_outline = vp_base.GetBoxOutline()
base_width = base_outline.MaximumPoint.X - base_outline.MinimumPoint.X

# Posición acumulada
current_x = base_center.X

for i in range(1, len(viewports)):

    vp = viewports[i]

    outline = vp.GetBoxOutline()
    width = outline.MaximumPoint.X - outline.MinimumPoint.X

    # Nueva posición X
    current_x = current_x + (base_width / 2) + separacion + (width / 2)

    old_center = vp.GetBoxCenter()

    new_center = XYZ(
        current_x,
        old_center.Y,
        old_center.Z
    )

    vp.SetBoxCenter(new_center)

    # Actualizar ancho base
    base_width = width

TransactionManager.Instance.TransactionTaskDone()

OUT = viewports