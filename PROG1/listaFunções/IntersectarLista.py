def intersectar_lista(lista, listab, listac):
    for elemento in listab:
        if elemento in lista:
            listac.append(elemento)

lista_A = [1, 2, 3, 4]
lista_B = [3, 4, 5, 6]
lista_C = []

intersectar_lista(lista_A, lista_B, lista_C)

print(lista_C)