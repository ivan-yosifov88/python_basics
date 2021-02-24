N1 = int(input())
N2 = int(input())
type_operator = input()
result = 0
even_or_odd = 0
if type_operator == "+":
     result = N1 + N2
elif type_operator == "-":
    result = N1 - N2
elif type_operator == "*":
    result = N1 * N2
elif type_operator == "/" and N2 != 0:
    result = N1 / N2
elif type_operator == "%" and N2 != 0:
     result = N1 % N2
else:
    pass
if type_operator == "+" or type_operator == "-" or type_operator == "*":
    if result % 2 == 0:
        even_or_odd = "even"
    else:
        even_or_odd = "odd"
    print(f"{N1} {type_operator} {N2} = {result} - {even_or_odd}")
elif type_operator == "/" and N2 != 0:
    print(f"{N1} / {N2} = {result:.2f}")
elif type_operator == "%":
    if N2 == 0:
        print(f"Cannot divide {N1} by zero")
    else:
        print(f"{N1} % {N2} = {result}")
elif type_operator == "/" and N2 == 0:
    print(f"Cannot divide {N1} by zero")