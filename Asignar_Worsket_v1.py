import sys
import clr

clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference('RevitServices')
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

doc = DocumentManager.Instance.CurrentDBDocument

# -------------------------------
# 🔹 INPUTS
# -------------------------------
listas_elementos = UnwrapElement(IN[0])
worksets_ids = IN[1]

# -------------------------------
# 🔹 NORMALIZAR LISTAS
# -------------------------------
if isinstance(listas_elementos, list):
    if len(listas_elementos) > 0 and not isinstance(listas_elementos[0], list):
        listas_elementos = [listas_elementos]
else:
    listas_elementos = [[listas_elementos]]

# -------------------------------
# 🔹 PROCESO
# -------------------------------
salida = []
errores = []

TransactionManager.Instance.EnsureInTransaction(doc)

i = 0
for lista in listas_elementos:

    # 🔹 Seguridad: evitar desbordes
    if i >= len(worksets_ids):
        errores.append("Falta Workset para índice: " + str(i))
        break

    ws = worksets_ids[i]

    # 🔹 Si viene como lista → tomar primer valor
    if isinstance(ws, list):
        if len(ws) > 0:
            ws = ws[0]
        else:
            errores.append("Workset vacío en índice: " + str(i))
            i += 1
            continue

    # 🔹 Convertir int → WorksetId
    if isinstance(ws, int):
        ws = WorksetId(ws)

    for ele in lista:
        try:
            if ele and isinstance(ele, RevitLinkInstance):

                # 🔹 Despin si es necesario
                if ele.Pinned:
                    ele.Pinned = False

                param = ele.get_Parameter(BuiltInParameter.ELEM_PARTITION_PARAM)

                if param and not param.IsReadOnly:

                    # DEBUG (opcional)
                    before = param.AsValueString()

                    param.Set(ws)

                    after = param.AsValueString()

                    salida.append({
                        "Id": ele.Id,
                        "Antes": before,
                        "Después": after
                    })

                else:
                    errores.append("ReadOnly o sin parámetro: " + str(ele.Id))

        except Exception as e:
            errores.append("Error en elemento {}: {}".format(ele.Id, str(e)))

    i += 1

TransactionManager.Instance.TransactionTaskDone()

# -------------------------------
# 🔹 OUTPUT
# -------------------------------
OUT = salida, errores
