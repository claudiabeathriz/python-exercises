# Escreva um programa que calcule o máximo divisor comum de dois números.

primeiro_numero = int(input('Digite um numero inteiro: '))
segundo_numero = int(input('Digite um numero inteiro: '))

while segundo_numero != 0:
    temp = segundo_numero
    segundo_numero = primeiro_numero % segundo_numero
    primeiro_numero = temp

print('MDC = ',primeiro_numero)