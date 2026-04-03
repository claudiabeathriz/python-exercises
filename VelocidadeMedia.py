# 3) Construa um programa que receba do usuário a variação do deslocamento de um objeto
# (em metros) e a variação do tempo percorrido (em segundo). Ao fim, o programa deve
# calcular a velocidade média, em m/s, do objeto.

deslocamento = float(input('Digite seu deslocamento em metros: '))
tempo = float(input('Digite a variação do tempo percorrido em segundos: '))

velocidadeMedia = deslocamento * tempo

print(f"Sua velocidade média foi de {velocidadeMedia}")
