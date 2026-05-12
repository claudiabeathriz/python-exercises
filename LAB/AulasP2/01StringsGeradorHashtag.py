# Criar um gerador de hashtags a partir de uma frase. A hashtag deve
# começar com #, ter todas as palavras juntas, e cada palavra deve iniciar
# com letra maiúscula.

# Frase original: 'python é uma linguagem de programação'
# Hashtag gerada: #PythonÉUmaLinguagemDeProgramação

frase_original = 'python é uma linguagem de programação'

frase_nova = '#' + frase_original.title().strip()
print(frase_nova)
# Saída vai ser errada, pois o strip() limpa apenas os espaços
# em branco no início e no final

hashtag = '#' + ''.join(frase_original.title().split())
print(hashtag)
# Saída vai ser correta, pois o split() divide a string em uma lista de palavras,
# e o join() junta as palavras sem espaço, indicando que o separador é '' (nada)
