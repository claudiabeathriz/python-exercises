arquivo = open('pessoas.dat', 'r')
total_mulheres = 0
total_homens = 0

for pessoas in arquivo:
    nome, email, sexo, idade = dados_pessoa = pessoas.split(',')
    print(nome, email, sexo, idade, sep="\t")

    if sexo == 'F':
        total_mulheres += 1
    else:
        total_homens += 1
print('Total de mulheres:', total_mulheres)
print('Total de homens:', total_homens)
arquivo.close()