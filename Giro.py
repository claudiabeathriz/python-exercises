# Peça ao usuário para inserir 5 números, que serão armazenados em uma lista.
# Em seguida, peça ao usuário um número inteiro N. O programa deve "girar"
# a lista para a direita N vezes. A cada giro, o último elemento se torna o primeiro.
# ● Exemplo:
# ○ Lista original: [10, 20, 30, 40, 50]
# ○ O usuário digita N = 2.
# ○ Após 1 giro: [50, 10, 20, 30, 40]
# ○ Após 2 giros (resultado final): [40, 50, 10, 20, 30]
# ○ Imprima a lista após a rotação completa.

lista = [10, 20, 30, 40, 50]

#while len(lista) < 5:
 #   numero = int(input('Digite o número: '))

  #  lista.append(numero)

print(lista)

N = int(input("Digite quantas vezes você quer girar: "))

for i in range(N):
    ultimo = lista.pop()
    lista.insert(0, ultimo)

print(lista)