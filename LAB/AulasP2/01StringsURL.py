# Dada uma URL completa, sua tarefa é extrair e exibir separadamente o
# protocolo, o domínio e o caminho (path).

url = "https://www.exemplo.com.br/produtos/eletronicos"

# Protocolo: https
# Dominio: www.exemplo.com.br
# Caminho: /produtos/eletronicos

protocolo = url[:5]
print("Protocolo: ", protocolo)

dominio = url[8:26]
print("Dominio: ", dominio)

caminho = url[26:]
print("Caminho: ", caminho)
