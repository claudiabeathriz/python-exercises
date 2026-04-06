# 7) Crie um programa que peça para o usuário digitar dois números. O programa deve então
# imprimir o resultado Booleano (True ou False) para cada uma das seguintes afirmações:
# ● O primeiro número é igual ao segundo.
# ● O primeiro número é diferente do segundo.
# ● O primeiro número é maior que o segundo.
# ● O primeiro número é menor ou igual ao segundo.

numero1 = float(input("Digite o primeiro numero: "))
numero2 = float(input("Digite o segundo numero: "))

print(f"O primeiro número é igual ao segundo: {numero1 == numero2}")
print(f"O primeiro número é diferente do segundo: {numero1 != numero2}")
print(f"O primeiro número é maior que o segundo: {numero1 > numero2}")
print(f"O primeiro número é menor que o segundo: {numero1 < numero2}")
