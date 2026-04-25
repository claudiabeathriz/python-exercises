arquivo = open('pessoas.dat', 'r')
total_mulheres = 0
total_homens = 0

for pessoas in arquivo:
    dados_pessoa = pessoas.split()
    nome = dados_pessoa[0]
    email = dados_pessoa[1]
    sexo = dados_pessoa[2]
    idade = dados_pessoa[3]

    if sexo == 'F':
        print(nome, email, sexo, idade, sep="\t")
        total_mulheres += 1
    else:
        total_homens += 1
    print('Total de mulheres:', total_mulheres)
    print('Total de homens:', total_homens)
    arquivo.close()