file = open('dados.txt', 'r', encoding="utf-8")
content = file.read()
for c in content:
    print(c)
file.close()
# file.read() reads all content and saves it as a string
# the for loop iterates over the string, so each c is a single character

file = open('dados.txt', 'r', encoding="utf-8")
for line in file:
    print(line, end="")
file.close()
# here, the file object itself is iterable
# each iteration returns one line at a time (split by '\n')
# so 'line' is a whole line, not a character
# print(line, end="") avoids adding extra newlines because lines already end with '\n'