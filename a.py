if 'IN' not in globals():
    IN = [None, None]

if 'OUT' not in globals():
    OUT = None
    
# para importar LookupParameter que tengo que importar import 
elements = IN[0] 
param_name = IN[1]

# 🔥 asegurar lista
if not isinstance(elements, list):
    elements = [elements]

# 🔥 unwrap seguro
elements = [UnwrapElement(e) for e in elements if e]

filtered = []

for e in elements:
    try:
        p = e.LookupParameter(param_name)
        
        if p:
            val = p.AsString()
            
            if val and val.strip().upper() == "MINIMO":
                filtered.append(e)
    except:
        # ignora elementos problemáticos
        continue

OUT = filtered