# 1) Considere o trecho de código escrito em Python apresentado abaixo para responder
# às perguntas seguintes.

def f(v):
    d = len(v)
    q=(v[0]+v[d-1])/2

    return q

n = int( input("Digite n:"))
x = []
for i in range(n//10,n):
    x.append(i*10)
y= f(x)

print(y)

# a) Qual é o tipo do dado armazenado na variável n? inteiro(int)
# b) Quantas funções foram declaradas? Identifique-as. 1 => def f(v)
# c) Cite um exemplo de entrada do usuário que levará este programa a um erro. 0, negativo, letras
# d) Caso um usuário digite 10 quando requisitado pelo programa, qual valor será
# atribuído à variável y? Justifique.
# 50.0
# 10 // 10 = 1
# range(1, 10)
# 1, 2, 3, 4, 5, 6, 7, 8, 9
# x = [10, 20, 30, 40, 50, 60, 70, 80, 90]
# d = len(v) → d = 9
# v[0] = 10
# v[d-1] = v[8] = 90
# q = (10 + 90) / 2
# q = 100 / 2
# q = 50.0
# y = f(x) que retorna q
