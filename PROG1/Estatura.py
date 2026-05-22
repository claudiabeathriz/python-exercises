# 2) Construa um programa que recebe a estatura de usuário em metros e converte para
# centímetros.
# Exemplo de saída: “Sua altura em centímetros é x.xx.”

estatura = float(input('Digite sua estatura em centímetros: '))

altura_m = estatura * 0.01

print(f"Sua altura em metros é {altura_m:.2f}m")