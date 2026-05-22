# Escreva um programa que utilize uma função para ler o nome, idade e o nível de uma pessoa, sendo que o nível poderia ser 1,2,3. o programa deverá ainda totalizar a quantidade de pessoas por nível e a média de idade.

def obterdados(): 
  nome = input("Informe seu nome: ")
  idade = int(input("Informe sua idade: ")
  nivel = int(input("Informe seu nível (1,2,3): ")
  return nome,idade,nivel
  
def cabecalho():
    print('UFF')
    print('PROG I')

totalpessoas_nivel1 = 0
totalpessoas_nivel2 = 0
totalpessoas_nivel3 = 0
somaidade = 0

nome,idade,nivel = obterdados()
while nivel != 0 and nome != "" and idade != 0:
  if nivel == 1: 
    totalpessoas_nivel1 += 1
  elif nivel == 2:
    totalpessoas_nivel2 += 1
  else:
    totalpessoas_nivel3 += 1
  somaidade += idade
  nome,idade,nivel = obterdados()

cabecalho()

print(total_pessoas_nivel1)
print(total_pessoas_nivel2)
print(total_pessoas_nivel3)

media = somaidade / (total_pessoa_nivel1 + total_pessoa_nivel2 + total_pessoa_nivel3)
print(media)


  
