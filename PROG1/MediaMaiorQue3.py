# Escreva um programa para ler vários valores inteiros e calcular a média de
# uma sequência de números. A finalização do conjunto de dados termina
# quando o usuário digitar 0 ou quando a média for maior 3.

qtd_numeros = 0
soma = 0
media =  0
valor = int(input('Digite um valor: (Digite 0 para encerrar)'))

while valor != 0 and media <= 3:
    qtd_numeros += 1
    soma += valor

    media = soma / qtd_numeros

    valor = int(input('Digite um valor: (Digite 0 para encerrar)'))

print(media)
print(soma)