first_number_upper_limit = int(input())
second_number_upper_limit = int(input())
third_number_upper_limit = int(input())
is_first_number = False
is_second_number = False
is_third_number = False
for first_number in range (1 , first_number_upper_limit + 1):
    if first_number % 2 == 0:
        is_first_number = True
    else:
        continue
    for second_number in range(1, second_number_upper_limit + 1):
        if second_number == 2 or second_number == 3 or second_number == 5 or second_number == 7:
            is_second_number = True
        else:
            continue
        for third_number in range(1, third_number_upper_limit + 1):
            if third_number % 2 == 0:
                is_third_number = True
            else:
                continue
            print(f"{first_number} {second_number} {third_number}")