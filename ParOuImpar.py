# Par ou Ímpar: Peça ao usuário um número inteiro. Verifique se o
# número é par ou ímpar e exiba a resposta. Dica: Um número é par
# se o resto da sua divisão por 2 for igual a 0 (numero % 2 == 0).

numero = int(input("Digite um numero inteiro: "))

if numero % 2 == 0:
    print("par")
else:
    print("impar")