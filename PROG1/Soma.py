arquivos = open("numeros.dat", "r", encoding="utf-8")
soma = 0

for i in arquivos:
    # valoresstr = arquivos.readline()
    num = int(i)
    soma += num

arquivos.close()
print(f"Soma: {soma}")