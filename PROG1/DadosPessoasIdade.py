arquivo = open('nomes.dat', 'r')

for dados in arquivo:
    dados = dados.strip('\n')
    nome, idadestr = dados.split(',')
    idade = int(idadestr)


