arquivo = open('nomes.dat', 'r')
nome = arquivo.readline()

def total_vogais(x):
    x = x.rstrip()
    count_vogais = 0
    vogais = 'AEIOUaeiou'
    i = 0
    while i< len(x) and x[i] != ' ':
        if x[i] in vogais:
            count_vogais += 1
        i = i + 1
    return count_vogais

while nome:

    nome = nome.strip('\n').rstrip().lstrip()
    total = total_vogais(nome)

    print('total de vogais: ', total)
    nome = arquivo.readline()

arquivo.close()