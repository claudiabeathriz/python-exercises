# Implemente uma forma simples de compressão de dados conhecida como Run-Length
# Encoding (RLE). A ideia é substituir sequências de caracteres repetidos pelo número de
# repetições seguido do próprio caractere. Por exemplo, a string AAAABBC seria comprimida
# para 4A2B1C.

# string_original = "WWWWBBWWWBWWWWWWWWWWWB"

string = input("Digite uma string (apenas letras): ")

resultado = ""
contador = 1

for i in range(len(string)):
    if i < len(string) - 1 and string[i] == string[i + 1]:
        contador += 1
    else:
        resultado += str(contador) + string[i]
        contador = 1

print("String comprimida:", resultado)
