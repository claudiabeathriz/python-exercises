# Uma empresa define o bônus de fim de ano com base no percentual de metas que um
# funcionário atingiu:
# ● Se atingiu mais de 100% da meta: bônus de 15% do salário.
# ● Se atingiu entre 80% e 100% (inclusive): bônus de 10% do salário.
# ● Se atingiu entre 50% e 79% da meta: bônus de 5% do salário.
# ● Abaixo de 50%: sem bônus.
# ● O programa coleta o salario e o percentual da meta_atingida.
# ● A estrutura if-elif-else verifica a meta_atingida em ordem decrescente.
# ● Assim que uma condição verdadeira é encontrada (por exemplo, meta_atingida é 95,
# que é >= 80), o bonus_percentual correspondente é definido e o resto da estrutura é
# ignorado.
# ● Se nenhuma das condições do if ou elif for verdadeira (ex: meta de 40%), o bloco else é
# executado.
# ● Por fim, o valor do bônus é calculado e uma mensagem apropriada é exibida.

salario = float(input("Digite seu salário: "))
meta_atingida = float(input("Digite a % da meta atingida: "))

if meta_atingida > 100:
    bonus = salario * 0,15
elif 80 <= meta_atingida <= 100:
    bonus = salario * 0.10
elif 50 <= meta_atingida < 79:
    bonus = salario * 0.05
else:
    bonus = 0

salario += bonus

print(salario)

