first_number = int(input())
second_number = int(input())
for number in range(first_number, second_number + 1):
    number_to_string = str(number)
    sum_of_even = 0
    sum_of_odd = 0
    for index, digit in enumerate(number_to_string):
        if index % 2 == 0:
            sum_of_even += int(digit)
        elif index % 2 == 1:
            sum_of_odd += int(digit)
    if sum_of_even == sum_of_odd:
        print(number, end= " ")

