# 4) Construa um programa para calcular a área e o perímetro do círculo.
# Exemplo de saída: “Área = xx.xx m2, Perímetro = xx.xx m.”

# Área = pi * r²
# Perímetro = 2 * pi * r
import math

raio = float(input("Digite o tamanho do raio do círculo: "))

area = math.pi * raio**2
perimetro = 2 * math.pi * raio

print(f"Área = {area:.2f} m2, Perímetro = {perimetro:.2f} m")