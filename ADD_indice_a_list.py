#Adicionar una lista en otra lista
list1 = IN[0] # lista
list2 = IN[1]

if not isinstance(list1, list):
    list1 = [list1]

if len(list2) > 0 and not isinstance(list2[0], list):
    list2 = [list2]
    
output = []

for i in range(len(list1)):
    #agrega el valor de list1 al inicio de cada sublista.
    newsub = [list1[i]] + list(list2[i])

    output.append(newsub)

OUT = output