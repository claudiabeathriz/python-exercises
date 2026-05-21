# 1) Você recebeu uma lista de strings, onde cada string contém o nome de um aluno,
# seguido por suas notas, separadas por vírgulas. Seu objetivo é processar esses dados para
# calcular a média de cada aluno e determinar seu status de aprovação. A média para
# aprovação é 7.0.

dados_alunos = [
    "Ana Silva: 8.5, 9.0, 7.5",
    "Bruno Costa: 6.0, 5.5, 7.0",
    "Carla Dias: 9.5, 10.0, 9.0"
    ]

for aluno in dados_alunos:
    nome, notas_str = aluno.split(":")
    notas = notas_str.split(",")

    notas_float = [] # depois passar str pra float
    for nota in notas:
        notas_float.append(float(nota)) # fazendo a conversão de type

    media = sum(notas_float) / len(notas_float)

    if media >= 7.0:
        status = "Aprovado"
    else:
        status = "Reprovado"

    print(f"Aluno: {nome}")
    print(f"Média: {media:.2f}")
    print(f"Status: {status}")