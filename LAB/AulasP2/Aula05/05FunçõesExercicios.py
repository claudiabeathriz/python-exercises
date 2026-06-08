# Escreva uma função que receba dois números e retorne True se o
# primeiro número for múltiplo do segundo.

def multiplo (x, y):
    if x % y == 0:
        return True
    else:
        return False
# return x % y == 0 => já vai retornar boolean

print(multiplo(2,3))

# Escreva uma função que receba o lado (L) de um quadrado e retorne
# sua área (A = L*L).

def area_quadrado(l):
    return l * l

print(area_quadrado(4))

# Escreva uma função que receba a base e a altura de um triângulo e
# retorne sua área (A = (base * altura)/2).

def area_triangulo(base, altura):
    return base * altura / 2

print(area_triangulo(4,5))