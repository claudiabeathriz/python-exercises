# Dadas duas listas de mesmo tamanho, crie um programa que gere uma terceira lista
# contendo os elementos das duas listas originais intercalados.
# ● Exemplo:
# ○ lista_a = ['a', 'c', 'e']
# ○ lista_b = ['b', 'd', 'f']
# ○ Resultado esperado: lista_c = ['a', 'b', 'c', 'd', 'e', 'f']

lista_a = ['a', 'c', 'e']
lista_b = ['b', 'd', 'f']

lista_c = []

for i in range(len(lista_a)):
    lista_c.append(lista_a[i])
    lista_c.append(lista_b[i])

lista_c.sort()

print(lista_c)