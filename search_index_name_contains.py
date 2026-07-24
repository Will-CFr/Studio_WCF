#Como int0 tenemos una lista y como int1 un texto, el cual se va a buscar en la lista, si el texto se encuentra en la lista, se devuelve el elemento de la lista que contiene el texto, si no se encuentra, se devuelve un mensaje de error.
lista = [0]
text = IN[1]

#caso de que list no sea una lista, lo convertimos en una lista con un solo elemento
if not isinstance(lista, list):
    lista = [lista]

indice = -1 # inicializamos el indice en -1 para indicar que no se ha encontrado el texto
enu = enumerate(lista) # enumeramos la lista para obtener el indice de cada elemento
for i, item in enu
    #verificamos si el texto está contenido en el elemento de la lista
    if text.lower() in item.lower(): # convertimos ambos a minúsculas para hacer la comparación sin importar mayúsculas o minúsculas
        indice = i # si se encuentra el texto, guardamos el indice
        break # salimos del ciclo una vez que encontramos el texto

OUT = indice # devolvemos el indice del elemento que contiene el texto, o -1 si no se encuentra el texto en la lista