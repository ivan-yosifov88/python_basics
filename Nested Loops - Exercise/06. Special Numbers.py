special_number = int(input())
for number in range(1111, 9999):
    is_number_special = True
    number_as_string = str(number)
    for digit in number_as_string:
        if int(digit) == 0:
            is_number_special = False
            break
        elif special_number % int(digit) != 0:
            is_number_special = False
            break
    if is_number_special:
        print(f"{number_as_string}", end=" ")

