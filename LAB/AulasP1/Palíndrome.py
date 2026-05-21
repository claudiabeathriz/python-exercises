def compara(a, b):
    if a < b:
        return '<'
    elif a > b:
        return '>'
    else:
        return '='

def palindromo_quebrado(palavra):
    palavra = palavra.upper()
    n = len(palavra)

    for i in range(n - 1):
        esquerda = compara(palavra[i], palavra[i + 1])
        direita = compara(palavra[n - 1 - i], palavra[n - 2 - i])

        if esquerda != direita:
            return False

    return True

# ===== INPUT DO USUÁRIO =====
palavra = input('Digite uma palavra: ')

# ===== SAÍDA =====
if palindromo_quebrado(palavra):
    print("É palíndrome quebrada.")
else:
    print("Não é palíndrome quebrada.")