# 1) Crie um programa que receba uma string como argumento e retorne o número de
# vogais (a, e, i, o, u) que ela contém.
# O programa deve funcionar tanto para maiúsculas quanto para minúsculas.

string = str(input("Digite uma string: ")).lower()
vogais = 0

for letra in string:
    # if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
    # sem lower() no input do usuario: if letra in "aeiouAEIOU":
    if letra in "aeiou":
        vogais += 1

print("Número de vogais: ", vogais)

# 2) Escreva um programa que peça uma palavra ao usuário e a imprima de trás para frente.
# ● Exemplo: Se o usuário digitar "Python", o programa deve imprimir "nohtyP".

palavra = str(input("Digite uma palavra: "))
invertida = palavra[::-1]
print(invertida)

# 3) Faça um programa que verifique se uma palavra digitada pelo usuário é um palíndromo.
# Um palíndromo é uma palavra que se lê da mesma forma de trás para frente.
# ● Exemplos: "arara", "ovo", "radar".

palavra = input("Digite uma palavra ou frase: ")
texto = palavra.lower().replace(" ", "")

if texto == texto[::-1]:
    print("É um palíndromo")
else:
    print("Não é um palíndromo")

# 4) Peça ao usuário para digitar uma frase. Seu programa deve contar e exibir quantas
# palavras existem nessa frase.

frase = input("Digite uma frase: ")
frase = frase.split(" ")
palavras = 0

for palavra in frase:
    palavras += 1

print(palavras)

# solução mais simples:
frase = input("Digite uma frase: ")
print(len(frase.split()))

# 5) Faça um programa que peça ao usuário para digitar um nome ou expressão (ex:
# "HyperText Markup Language"). O programa deve gerar e exibir um acrônimo pegando a
# primeira letra de cada palavra em maiúsculas (ex: "HTML").

frase = input("Digite um nome ou expressão: ")

acronimo = ""

for letra in frase:
     if letra.isupper():
         acronimo += letra

print(acronimo)

# 6) Peça ao usuário para inserir uma frase. O programa deve analisar a frase e exibir as
# seguintes informações:
# ● O número total de caracteres (incluindo espaços).
# ● O número de vogais.
# ● O número de consoantes.

frase = input("Digite uma frase: ")

caracteres = len(frase)
vogais = 0
consoantes = 0

for letra in frase:
    if letra.lower() in "aeiou":
        vogais += 1
    elif letra.isalpha():
        consoantes += 1

print("Caracteres:", caracteres)
print("Vogais:", vogais)
print("Consoantes:", consoantes)