"""
Exiba os índices da lista
"""
#        0       1       2
lista= ['Mary', 'ana', 'Luiz']
lista.append('fernando')

indices = range(len(lista))


for indice in indices:
    print(indice, lista[indice], type(lista[indice]))
