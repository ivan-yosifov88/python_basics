first_number = int(input())
second_number = int(input())
for first_digit in range(1, first_number + 1):
    for second_digit in range(1, first_number + 1):
        for third_digit in range(97, 97 + second_number):
            for fourth_digit in range(97, 97 + second_number):
                for fifth_digit in range(1, first_number + 1):
                    if fifth_digit > first_digit and fifth_digit > second_digit:
                        print(f"{first_digit}{second_digit}{chr(third_digit)}{chr(fourth_digit)}{fifth_digit}", end= " ")