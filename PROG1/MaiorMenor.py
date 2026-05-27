# Escreva um programa que leia uma sequência de valores inteiros, a
# finalização do conjunto de dados termina quando o usuário digitar 0, e:
# a) imprima todos os números; -> nao
# b) imprima o maior e o menor valor.
from cmath import inf

valor = int(input('Digite um valor: (Digite 0 para encerrar)'))

maior_valor = -inf;
menor_valor = inf;

while valor != 0:

    print(valor)

    if valor > maior_valor:
        maior_valor = valor

    if valor < menor_valor:
        menor_valor = valor

    valor = int(input('Digite um valor: (Digite 0 para encerrar)'))

print('O maior valor digitado foi ', maior_valor)
print('O menor valor digitado foi ', menor_valor)

print('Programa encerrado')
