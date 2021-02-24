text = input()
sum = 0
for simbol in text:
    if simbol == "a":
        sum += 1
    elif simbol == "e":
        sum += 2
    elif simbol == "i":
        sum += 3
    elif simbol == "o":
        sum += 4
    elif simbol == "u":
        sum += 5
print(sum)