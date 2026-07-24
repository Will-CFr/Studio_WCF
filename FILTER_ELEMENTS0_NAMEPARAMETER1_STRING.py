# -*- coding: utf-8 -*-

# IN[0] = Elementos
# IN[1] = Nombre del parámetro (ejemplo: "COSAPI-NIVEL")
# IN[2] = Texto a buscar (ejemplo: "MONTANTE")

import clr

clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

# Entradas
elements = UnwrapElement(IN[0])
paramName = IN[1]
searchText = IN[2]

# Asegurar lista
if not isinstance(elements, list):
    elements = [elements]

containsList = []
notContainsList = []

for elem in elements:
    
    try:
        param = elem.LookupParameter(paramName)
        
        if param:
            
            value = param.AsString()
            
            if value:
                
                if searchText in value:
                    containsList.append(elem)
                else:
                    notContainsList.append(elem)
            
            else:
                notContainsList.append(elem)
        
        else:
            notContainsList.append(elem)
            
    except:
        notContainsList.append(elem)

OUT = containsList, notContainsList