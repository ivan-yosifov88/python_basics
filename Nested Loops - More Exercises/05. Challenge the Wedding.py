number_of_men = int(input())
number_of_women = int(input())
number_of_tables = int(input())
is_tables_over = False
for men in range(1, number_of_men + 1):
    for women in range(1, number_of_women + 1):
        number_of_tables -= 1
        if number_of_tables < 0:
            is_tables_over = True
            break
        else:
            print(f"({men} <-> {women})", end = " ")
    if is_tables_over:
        break