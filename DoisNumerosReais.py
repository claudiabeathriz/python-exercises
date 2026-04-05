# 5) Construa um programa que leia 2 números reais informados pelo usuário. Ao fim, o
# programa deve calcular e imprimir:
# a) a soma dos dois valores;
# b) o produto entre eles;
# c) a divisão entre eles;
# d) o primeiro número elevado ao quadrado;
# e) a raiz quadrada do segundo número.

numero1 = float(input("Digite o primeiro numero: "))
numero2 = float(input("Digite o segundo numero: "))

soma = numero1 + numero2
produto = numero1 * numero2
divisao = numero1 / numero2
quadrado1 = numero1 ** 2
quadrado2 = numero2 ** 2

print(f"Soma: {soma:.2f}, produto: {produto:.2f}, divisão: {divisao:.2f}, quadrado do primeiro número: {quadrado1:.2f}, quadrado do segundo número: {quadrado2:.2f}")