# 8) Escreva um programa que tenha uma senha secreta armazenada em uma variável (ex:
# senha_secreta = "programar"). O programa deve solicitar que o usuário digite uma senha e,
# em seguida, imprimir na tela o resultado Booleano (True ou False) da comparação que
# verifica se a senha digitada é exatamente igual à senha secreta.
# ● Exemplo de execução:
# ○ Senha secreta no código: "programar"
# ○ Usuário digita: "python"
# ○ Programa imprime: False

senhaSecreta = "programar"

senhaUsuario = str(input("Diga sua senha: "))
print(senhaUsuario == senhaSecreta)