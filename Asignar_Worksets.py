import sys
import clr

clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *
from Autodesk.Revit.DB.Structure import *

clr.AddReference('RevitAPIUI')
from Autodesk.Revit.UI import *

clr.AddReference('System')
from System.Collections.Generic import List

clr.AddReference('RevitServices')
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

doc = DocumentManager.Instance.CurrentDBDocument


# The inputs to this node will be stored as a list in the IN variables.
dataEnteringNode = IN

# Place your code below this line

listas_elementos = UnwrapElement(IN[0])
worksets_ids = IN[1]

#Do some action in a Transaction
i = 0
#asig_bien = 0
salida = []
if listas_elementos != None:
	TransactionManager.Instance.EnsureInTransaction(doc)
	for lista in listas_elementos:
		for ele in lista:
			ele_workset = ele.LookupParameter("Workset")
			ele_workset.Set(worksets_ids[i])
			salida.append(ele)
		i+=1	
	TransactionManager.Instance.TransactionTaskDone()		

# Place your code below this line

# Assign your output to the OUT variable.
#OUT = salida
OUT = salida