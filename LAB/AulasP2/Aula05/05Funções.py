# Funções servem como solução ao problema da repetição de
# código, além de ajudarem na generalização e modularização dos
# programas.

# Uma função deve resolver apenas um problema e, quanto mais
# genérica for sua solução, melhor ela será a longo prazo.
# Para saber se a sua função resolve apenas um problema, tente defini-la
# sem utilizar a conjunção “e”. Se ela faz isso e aquilo, já é um indicativo
# que efetua mais de uma tarefa e que talvez tenha que ser
# desmembrada em outras funções.

# Uma variável global é definida fora de uma função => Apesar de ser possível
# usar variáveis globais dentro de funções, esta é considerada uma péssima prática de programação.

def encontra_maior( x, y ): # x e y são os parâmetros de entrada
    m = x # variável local - uma variável local a uma função existe apenas dentro dela
    if y > x:
        m = y #variável local
    return m # saída/ retorno

a = int( input("Digite um inteiro: ") )
b = int( input("Digite um inteiro: ") )
c = int( input("Digite um inteiro: ") )
d = int( input("Digite um inteiro: ") )

maior = encontra_maior(a,b) # chamada de função
maior = encontra_maior(maior,c) # chamada de função
maior = encontra_maior(maior,d) # chamada de função

print(f"O maior número é: {maior}")