number = int(input())
number_for_printing = 1
for row in range(1, number + 1 ):
    for column in range(1, row + 1):
        print(f"{number_for_printing}", end= " ")
        number_for_printing += 1
        if number_for_printing > number:
            break
    if number_for_printing > number:
        break
    print()
