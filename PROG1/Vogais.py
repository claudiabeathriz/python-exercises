string = str(input("Digite a string:"))
print(string)

def total_vogais(x):
    x = x.rstrip()
    count_vogais = 0
    vogais = 'AEIOUaeiou'
    i = 0
    while i< len(x) and x[i] != ' ':
        if x[i] in vogais:
            count_vogais += 1
        i = i + 1
    return count_vogais

total = total_vogais(string)
print(total)