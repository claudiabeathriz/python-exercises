from urllib.parse import urlparse

url = "https://chatgpt.com/c/6a0da19e-4944-83e9-89de-68201c98eb9d"

resultado = urlparse(url)

print("Protocolo:", resultado.scheme)
print("Domínio:", resultado.netloc)
print("Caminho:", resultado.path)