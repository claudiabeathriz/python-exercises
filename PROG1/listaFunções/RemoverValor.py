# Rescreva o programa abaixo que exclui o primeiro elemento da lista com
# valor especificado, mas utilizando uma função.

def remover_valor(lista, valor):
    removeu = False
    temp = []

    for elemento in lista:
        if elemento != valor or removeu:
            temp.append(elemento)
        else:
            removeu = True

    return temp

lista = [1,4,5,6,4,7]

print(remover_valor(lista,4))

