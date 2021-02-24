number = int(input())
for numbers in range(1000, 10000):
    numbers_as_string = str(numbers)
    is_number_valid = True
    sum_digit_1 = 0
    sum_digit_2 = 0
    for index, digit in enumerate(numbers_as_string):
        if int(digit) == 0:
            is_number_valid = False
            break
        else:
            if 0 <= index <= 1:
                sum_digit_1 += int(digit)
            if 2 <= index <= 3:
                sum_digit_2 += int(digit)
    if is_number_valid:
        if sum_digit_1 == sum_digit_2 and number % sum_digit_1 == 0:
            print(numbers, end = " ")