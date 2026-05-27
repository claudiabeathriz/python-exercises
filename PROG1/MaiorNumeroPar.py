# Escreva um programa que leia uma sequência de valores inteiros, a
# finalização do conjunto de dados termina quando o usuário digitar 0, e:
# a) imprima todos os números; -> nao foi feito na resolução dele
# b) imprima o maior número par;

valor = int(input('Digite um número (0 para encerrar): '))

maior_par = None

while valor != 0:

    print(valor)

    if valor % 2 == 0:

        if maior_par is None or valor > maior_par:
            maior_par = valor

    valor = int(input('Digite um número (0 para encerrar): '))

if maior_par is not None:
    print('Maior número par:', maior_par)
else:
    print('Nenhum número par foi digitado.')