# faça um programa que leia um arquivo contendo o nome
# de varias pessoas e pra cada uma delas informe
# a qtd de vogais no primeiro nome
# primeiro nome separado do espaço em branco

arquivo = open('nomes.dat', 'r')

def total_vogais(primeiro_nome):
    count_vogais = 0
    vogais = 'AEIOUaeiou'

    for letra in primeiro_nome:
        if letra in vogais:
            count_vogais += 1

    return count_vogais

for linha in arquivo:
    linha = linha.strip()  # remove \n

    if linha == '':  # ignora linha vazia
        continue

    primeiro_nome = linha.split(' ')[0]

    total = total_vogais(primeiro_nome)

    print(f'{primeiro_nome}: {total} vogais')

arquivo.close()