# 2) Construa um programa que recebe a estatura de usuário em metros e converte para
# centímetros.
# Exemplo de saída: “Sua altura em centímetros é x.xx.”

estatura = float(input('Digite sua estatura: '))

altura_cm = estatura * 100

print(f"Sua altura em centímetros é {altura_cm:.2f}")