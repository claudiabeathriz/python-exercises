# Exemplos de criação de strings
nome = 'Maria'
frase = "Python e uma linguagem de programacao poderosa."
poema = """O sol brilha no céu azul,
e as nuvens dançam ao sabor do vento.
"""

print (nome)
print(frase)
print (poema)

# Strings em Python é são imutáveis. Uma vez que uma string é criada, ela não
# pode ser alterada

# Metodo len()
exemplo = "Ola, Mundo!"
tamanho = len(exemplo)
print(f"A string '{exemplo}' tem {tamanho} caracteres.")
# Saída: A string 'Olá, Mundo! tem 11 caracteres.

# Capitalização
texto = "o RATO roeu a ROUPA do rei de roma."

print("Original:", texto)
print("upper():", texto.upper()) # Saída: 0 RATO ROEU A ROUPA DO REI DE ROMA.
print("lower():", texto. lower()) # Saída: o rato roeu a roupa do rei de roma.
print("capitalize():", texto.capitalize()) # Saida: 0 rato roeu a roupa do rei de roma.
print("title():", texto.title()) # Saída: 0 Rato Roeu A Roupa Do Rei De Roma.

# Metodo strip() - limpando espaços em branco
email = " contato@exemplo.com "
print(f"'{email.strip()}'") # Saida: 'contato@exemplo.com' (todos)
print(f"'{email.lstrip()}'") # Saida: 'contato@exemplo.com ' (esquerda)
print(f"{email.rstrip()}'") # Saida: ' contato@exemplo.com' (direita)

# Metodo replace()
frase = "Eu gosto de cachorros."
nova_frase = frase. replace("cachorros", "gatos")
print(nova_frase) # Saida: Eu gosto de gatos.

# Metodo split()
data = "03/10/2025"
lista_data = data.split('/')
print(lista_data) # Saída: ['03', '10', '2025']

frase_linguagens = "Python, Java, C++, JavaScript"
lista_linguagens = frase_linguagens.split(', ')
print(lista_linguagens) # Saida: ['Python', 'Java', C++','JavaScript']

# Metodo join()
palavras = ["Python", "é", "incrivel"]
frase_unida = " ".join(palavras)
print(frase_unida) # Saída: Python é incrivel

# Metodos find() e count()
texto = "0 rato roeu a roupa do rei de Roma. 0 rato era rapido."

# Usando find()
posicao_rato = texto.find("rato")
print(f"A primeira ocorrência de 'rato' está no indice: {posicao_rato}") # Saída: 2

posicao_gato = texto.find("gato")
print(f"A posição de 'gato' é: {posicao_gato}") # Saída: -1 (não encontrado)

# Usando count()
contagem_rato = texto.count("rato")
print(f"A palavra 'rato' aparece {contagem_rato} vezes.") # Saida: 2

# Metodos in() e not in()
frase = "Bem-vindo ao mundo do Python"

print("'Python' in frase:", 'Python' in frase) # Saida: True
print("'Java' in frase:", 'Java' in frase) # Saída: False
print("'mundo' not in frase:", 'mundo' not in frase) # Saida: False

# Slicing
# Indices: P  y  t  h  o  n
#          0  1  2  3  4  5
#         -6 -5 -4 -3 -2 -1

palavra = "Python"

# Exemplos de Slicing
print (palavra[0:2]) # Pega do índice 0 até o 1 (o 2 é exclusivo) -> 'Py'
print (palavra[2:5]) # Pega do indice 2 ate o 4 -> 'tho'
print (palavra[:3]) # Pega do início até o indíce 2 -> 'Pyt'
print (palavra[3:]) # Pega do índice 3 até o final -> 'hon'
print (palavra[-3:]) # Pega os 3 últimos caracteres -> 'hon'
print (palavra[:]) # Cria uma cópia da string inteira -> 'Python'
print (palavra[ :: 2]) # Pega caracteres com passo 2 (do início ao fim) -> 'Pto'
print (palavra[ ::- 1]) # Inverte a string -> 'nohtyP'

palavra_amor = 'amor'
print (palavra_amor[0:4:2])
