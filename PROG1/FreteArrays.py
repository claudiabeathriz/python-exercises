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

fretes = {
    "sudeste": 15,
    "sul": 20,
    "nordeste": 25,
    "centro-oeste": 22,
    "norte": 30
}

regiao = str(input("Digite sua região: ").lower())

if regiao in fretes:
    print(f"Frete: R$ {fretes[regiao]:.2f}")
else:
    print("Entrega não disponível nessa região")