# Faça um Programa que peça os 3 lados de um triângulo. O programa
# deverá informar se os valores podem ser um triângulo. Indique, caso
# os lados formem um triângulo, se o mesmo é: equilátero, isósceles
# ou escaleno.
# Dicas:
# Três lados formam um triângulo quando a soma de quaisquer
# dois lados for maior que o terceiro;
# Triângulo Equilátero: três lados iguais;
# Triângulo Isósceles: quaisquer dois lados iguais;
# Triângulo Escaleno: três lados diferentes.

ladoA = float(input("Digite o primeiro lado do triangulo: "))
ladoB = float(input("Digite o segundo lado do triangulo: "))
ladoC = float(input("Digite o terceiro lado do triangulo: "))

if (ladoA + ladoB) > ladoC and (ladoB + ladoC) > ladoA and (ladoA + ladoC) > ladoB:
    if(ladoA == ladoB == ladoC):
        print("Triangulo Equilatero")
    elif ladoA == ladoB or ladoB == ladoC or ladoC == ladoA:
        print("Triangulo Isosceles")
    else:
        print("Triangulo Escaleno")
else:
    print("Não é Triangulo")