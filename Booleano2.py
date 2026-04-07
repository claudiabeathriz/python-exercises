# 7) Crie um programa que peça para o usuário digitar dois números. O programa deve então
# imprimir o resultado Booleano (True ou False) para cada uma das seguintes afirmações:
# ● O primeiro número é igual ao segundo.
# ● O primeiro número é diferente do segundo.
# ● O primeiro número é maior que o segundo.
# ● O primeiro número é menor ou igual ao segundo.

numero1 = float(input("Digite o primeiro numero: "))
numero2 = float(input("Digite o segundo numero: "))

print(f"{numero1} é igual a {numero2}: {numero1 == numero2}")
print(f"{numero1} é diferente de {numero2}: {numero1 != numero2}")
print(f"{numero1} é maior que {numero2}: {numero1 > numero2}")
print(f"{numero1} é menor que {numero2}: {numero1 < numero2}")