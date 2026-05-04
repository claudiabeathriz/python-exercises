# Escreva um programa para somar um conjunto de números pares fornecidos
# pelo usuário. A finalização do conjunto de dados termina quando o usuário
# digitar 0. Considere que números ímpares também podem ser fornecidos na
# entrada.

soma = 0

while True:

    numero = int(input('Digite um numero: (0 para encerrar)'))
    if numero == 0:
        break

    if numero % 2 == 0:
        soma += numero

print(soma)