"""
Cuidados com dados mutaveis
= - copiado o valor (imutavéis)
= - apronta para o mesmo valor na memória (Mutavel)

"""
lista_a = ['Luiz', 'maria']
lista_b = lista_a.copy()

lista_a[0] ='Qualquer coisa'
print(lista_b)
print(lista_a)
