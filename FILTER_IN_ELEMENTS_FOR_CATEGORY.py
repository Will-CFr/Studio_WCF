# Entradas
elementos = IN[0]
categoria = IN[1]

# Asegurar que la entrada sea una lista
if not isinstance(elementos, list):
    elementos = [elementos]

filtrados = []
resto = []

for e in elementos:
    try:
        if e.Category and e.Category.Name == categoria:
            filtrados.append(e)
        else:
            resto.append(e)
    except:
        resto.append(e)

# Salidas
OUT = filtrados, resto