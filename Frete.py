# Uma loja online precisa calcular o valor do frete de uma entrega com base na região do país
# informada pelo cliente. Cada região tem um valor de frete fixo.
# ● Sudeste: R$ 15,00
# ● Sul: R$ 20,00
# ● Nordeste: R$ 25,00
# ● Centro-Oeste: R$ 22,00
# ● Norte: R$ 30,00
# O programa deve perguntar a região do cliente e informar o valor do frete. Se a região
# digitada não for válida, o programa deve informar que a entrega não está disponível para
# aquela localidade.

regiao = str(input("Digite sua região: ").lower())

if regiao == "sudeste":
    print("Frete: R$ 15,00")
elif regiao == "sul":
    print("Frete: R$ 20,00")
elif regiao == "nordeste":
    print("Frete: R$ 25,00")
elif regiao == "centro-oeste":
    print("Frete: R$ 22,00")
elif regiao == "norte":
    print("Frete: R$ 30,00")
else:
    print("A entrega não está disponível nessa região")