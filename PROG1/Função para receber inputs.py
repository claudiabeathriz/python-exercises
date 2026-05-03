# Escreva um programa que utilize uma função para ler o nome,
# idade e o nível de uma pessoa, sendo que o nível poderia ser 1,2,3.
# O programa deverá ainda totalizar a quantidade de pessoas por nível
# e a média de idade.

def obterdados(): 
  nome = input("Informe seu nome: ")
  idade = int(input("Informe sua idade: "))
  nivel = int(input("Informe seu nível (1,2,3): "))
  return nome,idade,nivel
  
def cabecalho():
    print('UFF')
    print('PROG I')

total_pessoas_nivel1 = 0
total_pessoas_nivel2 = 0
total_pessoas_nivel3 = 0
soma_idade = 0

nome,idade,nivel = obterdados()
while nivel != 0 and nome != "" and idade != 0:
  if nivel == 1: 
    total_pessoas_nivel1 += 1
  elif nivel == 2:
    total_pessoas_nivel2 += 1
  else:
    total_pessoas_nivel3 += 1
  soma_idade += idade
  nome,idade,nivel = obterdados()

cabecalho()

print(total_pessoas_nivel1)
print(total_pessoas_nivel2)
print(total_pessoas_nivel3)

media = soma_idade / (total_pessoas_nivel1 + total_pessoas_nivel2 + total_pessoas_nivel3)
print(media)


  
