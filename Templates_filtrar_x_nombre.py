import clr
#Para filtra los templates IN0 por nombre que contiene In1
templates = IN[0]
texto_buscar = IN[1]

templates_filtrados = []
templates_sin_texto = []

#usamos for para recorrer la lista de templates y filtrar por nombre
for template in templates:
    nombre = template.Name