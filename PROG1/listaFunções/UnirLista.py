def unir_lista(listaa,listab):
    listac = listaa
    for elemento in listab:
        if elemento not in listac:
            listac.append(elemento)

    return listac

listaa = [1, 2, 3]
listab = [3, 4, 5]

resultado = unir_lista(listaa, listab)

print(resultado)