# Crie uma ferramenta para criptografar e descriptografar mensagens usando a Cifra de
# César, uma técnica de substituição simples em que cada letra de um texto é "deslocada" um
# certo número de posições no alfabeto.
# Etapas:
# ● Criar três variáveis
# ○ mensagem: a string a ser criptografada.
# ○ chave: um número inteiro que define o deslocamento.
# ○ modo: uma string que pode ser "criptografar" ou "descriptografar".
# ● Ignorar espaços e pontuações, mantendo-os como estão.
# ● Funcionar apenas para letras do alfabeto (sem acentos).
# ● Garantir que o alfabeto seja circular (depois de 'z' vem 'a').
# ● Se o modo for "descriptografar", o processo deve ser o inverso.

mensagem = str(input("Digite uma mensagem: "))
chave = int(input("Digite uma chave: "))
modo = input("Digite um modo (c/d): ").lower()

alfabeto = "abcdefghijklmnopqrstuvwxyz"

resultado = ""

for caractere in mensagem:
    if caractere.lower() in alfabeto:
        posicao = alfabeto.index(caractere.lower())

        if modo == "c":
            nova_posicao = (posicao + chave) % 26
        elif modo == "d":
            nova_posicao = (posicao - chave) % 26

        nova_letra = alfabeto[nova_posicao]

        if caractere.isupper():
            resultado += nova_letra.upper()
        else:
            resultado += nova_letra
    else:
        resultado += caractere  # mantém espaço, pontuação, números etc.

print("Resultado:", resultado)