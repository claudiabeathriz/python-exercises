# Escreva um programa que funcione como uma calculadora de média para um aluno. O
# programa deve pedir para o usuário digitar as notas uma a uma. O usuário poderá inserir
# quantas notas desejar. Para encerrar a inserção de notas, o usuário deve digitar -1. Após a
# inserção ser encerrada, o programa deve calcular e exibir a média das notas inseridas.
# ● Dica: Use um laço while que continue executando enquanto a nota digitada for
# diferente de -1. Armazene as notas em uma lista.

notas = []

while True:
    nota = float(input("Digite sua nota (-1 para sair): "))

    if nota == -1:
        break

    notas.append(nota)

if len(notas) > 0:
    media = sum(notas) / len(notas)
    print(f"Média: {media:.2f}")
else:
    print("Nenhuma nota foi inserida.")