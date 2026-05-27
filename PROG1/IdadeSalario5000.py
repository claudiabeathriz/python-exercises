# Escreva um programa que leia uma sequência de dados (idade, salário) de
# pessoas e imprima o total de pessoas com salário maior que R$ 5000,00 e
# idade < 40; a finalização do conjunto de dados termina quando o usuário
# digitar 0 para a idade.

total_de_pessoas = 0

idade = int(input('Digite sua idade: (Digite 0 para encerrar)'))

while idade != 0:
    salario = int(input('Digite seu salário: '))

    if idade < 40 and salario > 5000:
        total_de_pessoas += 1

    idade = int(input('Digite sua idade: (Digite 0 para encerrar)'))

print(total_de_pessoas)

