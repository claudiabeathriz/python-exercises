# Rescreva o programa abaixo que procure em uma lista um valor fornecido e
# retorne posição onde ele foi encontrado ou -1 caso não esteja na lista, mas
# utilizando uma função
#
def retornar_pos(lista,valor):
    for i in range(len(lista)):
        if lista[i] == valor:
            return i
    return -1

lista = [1, 2, 10, 5, 20]
valor = 10

print(retornar_pos(lista,valor))