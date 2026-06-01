# Rescreva o programa abaixo que exclui um elemento da lista em uma
# determinada posição e obter o valor excluído, mas utilizando uma função.

def obter_valor_removido(lista, pos):
    temp = []
    for i in range(len(lista)):
        if i != pos:
            temp.append(lista[i])
        else:
            elementoRetirado = lista[i]
    return temp, elementoRetirado

lista = [1, 2, 3, 4]
pos = 2
elementoRetirado = 0

print(lista)
print(obter_valor_removido(lista, pos))