# 2) Escreva uma função em Python que receba uma lista de números e
# retorne o maior número presente no lista.

def maior_numero(lista):
    m = lista[0]

    for num in lista:
        if num > m:
            m = num

    return m

entrada = input("Digite números separados por espaço: ")
lista = []

for x in entrada.split():
    x = int(x)
    lista.append(x)

maior = maior_numero(lista)

print("O maior número é: ", maior)