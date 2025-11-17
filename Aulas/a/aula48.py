"""
Lista em python
Tipo list - Mutável (Matriz)
Suporta vários tipos de valores de qualquer tipo 
Conhecimento reutilizáveis - indices de fatiamento
Métodos úteis : append, insert, pop, del, clear, exten, +
"""

#       +01234
#       *54321

string= 'ABCDE' # 5 caracteres (len)

# item:   0   1      2     3     4
#indice:  -5   -4    -3   -2   -1

Lista = [123, True, 'Ana', 1.2, []] 
#print(bool(Lista))
#print(Lista, type(Lista))

Lista[-3] = 'Maria'
print(Lista)
print(Lista[2] , type(Lista[2]))

