import clr

# Revit API
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

# Revit Services
clr.AddReference('RevitServices')
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

doc = DocumentManager.Instance.CurrentDBDocument

view = UnwrapElement(IN[0])
pipes = UnwrapElement(IN[1])
tagType = UnwrapElement(IN[2])

createdTags = []

TransactionManager.Instance.EnsureInTransaction(doc)

for i, pipe in enumerate(pipes):

    try:
        curve = pipe.Location.Curve

        # 0.2 pares / 0.3 impares
        t = 0.2 if i % 2 == 0 else 0.3

        midpoint = curve.Evaluate(t, True)

        ref = Reference(pipe)

        tag = IndependentTag.Create(
            doc,
            tagType.Id,
            view.Id,
            ref,
            False,
            TagOrientation.Horizontal,
            midpoint
        )

        createdTags.append(tag)

    except:
        createdTags.append(None)

TransactionManager.Instance.TransactionTaskDone()

OUT = createdTags