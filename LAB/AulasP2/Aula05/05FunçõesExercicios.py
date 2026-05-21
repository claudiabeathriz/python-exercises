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

# 1) Crie uma função chamada potencia que receba dois números: a base e o expoente.
# ● Regra: Não é permitido usar o operador de potência nem a função pow(). Deve
# implementar o cálculo utilizando um laço.
# ● Desafio: Garanta que a função funcione se o expoente for 0 (resultado deve ser 1).

def potencia (base, expoente):
    resultado = 1

    while expoente > 0:
        resultado = resultado * base
        expoente = expoente - 1

    return resultado

print(potencia(3,4))

# 2) Crie uma função chamada media_ponderada que receba uma lista de tuplas, onde cada
# tupla contém (nota, peso). A função deve calcular e retornar a média ponderada.
# ● Exemplo de entrada: [(8.0, 2), (9.0, 3), (7.0, 5)]



# 3) Escreva uma função chamada filtrar_por_genero que receba uma lista de dicionários
# (onde cada dicionário representa um livro com titulo e genero) e uma string com o
# genero_alvo.
# ● Saída: A função deve retornar uma nova lista contendo apenas os títulos dos livros
# que pertencem ao gênero solicitado.
# ● Exemplo de Entrada: livros = [{"titulo": "O Hobbit", "genero": "Fantasia"}, {"titulo":
# "Duna", "genero": "Sci-Fi"}]
#
# 4)
# ● Crie um pequeno "banco de dados" de alunos usando um dicionário aninhado. A
# chave principal será a matrícula do aluno (um inteiro), e o valor será outro dicionário
# contendo as informações ("nome" e "curso").
# ● Crie uma função adicionar_aluno que recebe o BD, matrícula, nome e curso e
# adiciona um novo aluno ao BD. A função deve verificar se a matrícula já existe antes
# de adicionar. Se existir, deve retornar False. Se for adicionado, deve retornar True.
# ● Crie uma função buscar_nome_curso que recebe o BD e a matrícula. A função deve
# retornar o nome do aluno e o curso dele, usando uma tupla (nome, curso). Se a
# matrícula não for encontrada, deve retornar (None, None).