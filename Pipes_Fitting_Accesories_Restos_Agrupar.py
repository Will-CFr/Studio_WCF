# Importar librerías
import clr

# Revit API
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *
from Autodesk.Revit.DB.Plumbing import Pipe

clr.AddReference('RevitNodes')
import Revit
clr.ImportExtensions(Revit.Elements)

# Entrada
elements = IN[0]

# Asegurar lista
if not isinstance(elements, list):
    elements = [elements]

# Listas
pipes = []
pipeFittings = []
pipeAccessories = []
mechanicalEquipment = []
others = []

# Recorrer elementos
for elem in elements:
    
    revitElem = elem.InternalElement
    
    added = False
    
    # Pipes
    if isinstance(revitElem, Pipe):
        pipes.append(elem)
        added = True
    
    # Family Instances
    elif isinstance(revitElem, FamilyInstance):
        
        category = revitElem.Category
        
        if category:
            
            catId = category.Id.IntegerValue
            
            # Pipe Fittings
            if catId == int(BuiltInCategory.OST_PipeFitting):
                pipeFittings.append(elem)
                added = True
            
            # Pipe Accessories
            elif catId == int(BuiltInCategory.OST_PipeAccessory):
                pipeAccessories.append(elem)
                added = True
            
            # Mechanical Equipment
            elif catId == int(BuiltInCategory.OST_MechanicalEquipment):
                mechanicalEquipment.append(elem)
                added = True
    
    # Elementos restantes
    if not added:
        others.append(elem)

# Salidas
OUT = (
    pipes,                 # OUT[0]
    pipeFittings,          # OUT[1]
    pipeAccessories,       # OUT[2]
    mechanicalEquipment,   # OUT[3]
    others                 # OUT[4]
)