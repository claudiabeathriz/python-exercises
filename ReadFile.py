file = open('dados.txt', 'r', encoding="utf-8")
line = file.readline()
while line:
    print(line, end="")
    line = file.readline()