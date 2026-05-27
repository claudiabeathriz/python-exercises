# Escreva um programa para ler vários valores inteiros e calcular a média de
# uma sequência de números. A finalização do conjunto de dados termina
# quando o usuário digitar 0.

valor = int(input("Digite um valor inteiro: "))

soma_valores = 0
qtd_valores = 0

while valor != 0:
    soma_valores += valor
    qtd_valores += 1
    valor = int(input("Digite um valor inteiro: "))

media = soma_valores / qtd_valores
print(media)