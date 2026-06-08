# 1) Crie uma lista que armazene 3 tuplas, onde cada tupla representa uma coordenada (lat,
# long). Peça ao usuário para digitar uma nova coordenada, verifique se ela já existe na lista e
# exiba uma mensagem de "Local já registrado" ou "Novo local adicionado".

coordenadas = [(0,0),
               (1,1),
               (2,2)]

lat = float(input("Digite a latitude: "))
long = float(input("Digite a longitude: "))

nova_coordenada = (lat,long)

if nova_coordenada in coordenadas:
    print("Local já registrado")
else:
    print("Novo local registrado")
    coordenadas.append(nova_coordenada)

print(coordenadas)

# 2) Crie uma tupla contendo os números por extenso de "Zero" a "Dez". Peça ao usuário um
# número inteiro pelo teclado e exiba o nome dele consultando a tupla.

numeros = ("zero",
           "um",
           "dois",
           "três",
           "quatro",
           "cinco",
           "seis",
           "sete",
           "oito",
           "nove",
           "dez")

num = int(input("Digite um numero: "))

if 0 <= num <= 10:
    print("O número digitado foi:", numeros[num])
else:
    print("Número fora do intervalo")

# 3) Crie dois conjuntos: alunos_segunda e alunos_quarta, contendo nomes de alunos que
# compareceram a essas aulas. Exiba:
# ● Os alunos que vieram em ambos os dias.
# ● Os alunos que vieram apenas na segunda.
# ● A lista completa de alunos distintos que assistiram a pelo menos uma aula.

alunos_segunda = {"Ana", "Bia", "Claudia"}
alunos_quarta = {"Claudia", "Marcos", "Lucas"}

print(f"Ambos: {alunos_segunda & alunos_quarta}")
print(f"Segunda: {alunos_segunda}")
print(f"Distintos: {alunos_segunda | alunos_quarta}")

# 4) Peça ao usuário para digitar um texto curto. Transforme o texto em uma lista de palavras
# e use um conjunto para contar quantas palavras únicas ele utilizou.

texto = (input("Digite um texto curto: "))

lista = texto.split()
conj = set(lista)

print("Palavras únicas:", conj)
print("Quantidade de palavras únicas:", len(conj))

# 5) Crie um dicionário que armazene o nome, o preço e a quantidade em estoque de um
# produto. Peça ao usuário para atualizar o preço e exiba o dicionário atualizado.

estoque = {"Produto": "Celular",
           "Preço": 4000.00,
           "Quantidade": 10}

estoque["Preço"] = float(input("Digite o novo preço do produto:"))
print(estoque)

# 6) Escreva um programa que receba uma string e crie um dicionário onde as chaves são os
# caracteres e os valores são a quantidade de vezes que cada caractere aparece na string.

string = str(input("Digite uma string: ")).lower()
dicionario = {}

for caractere in string:
    if caractere != " ":
        dicionario[caractere] = dicionario.get(caractere, 0) + 1

print(dicionario)

# 7) Crie um dicionário onde as chaves são nomes de alunos e os valores são listas contendo
# 3 notas. O programa deve percorrer o dicionário e exibir o nome de cada aluno junto com a
# sua média aritmética.

notas = {"Claudia": [10.0, 10.0, 10.0],
         "Ana": [6.0, 9.0, 7.5],
         "Bia": [5.0, 10.0, 8.5]}

for nome, nota in notas.items():
    print(f"Aluno: {nome};", f"Nota: {nota}")