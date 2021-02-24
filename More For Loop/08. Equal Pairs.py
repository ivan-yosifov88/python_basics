import sys

number = int(input())
first_number = int(input())
second_number = int(input())
first_sum = first_number + second_number
difference = 0
max_difference = - sys.maxsize
for numbers in range(number - 1):
    first_new_number = int(input())
    second_new_number = int(input())
    current_sum = first_new_number + second_new_number
    if first_sum != current_sum:
        difference = abs(first_sum - current_sum)
        if difference > max_difference:
            max_difference = difference
    first_sum = current_sum
if max_difference == 0:
    print(f"Yes, value = {first_sum}" )
else:
    print(f"No, maxdiff = {max_difference}")


