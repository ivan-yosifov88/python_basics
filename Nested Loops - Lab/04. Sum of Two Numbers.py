first_interval = int(input())
second_interval = int(input())
magic_number = int(input())
combination_counter = 0
is_combination_found = False
for first_number in range(first_interval, second_interval + 1):
    for second_number in range(first_interval, second_interval + 1):
        combination_counter += 1
        sum = first_number + second_number
        if sum == magic_number:
            print(f"Combination N:{combination_counter} ({first_number} + {second_number} = {magic_number})")
            is_combination_found = True
            break
    if is_combination_found:
        break
else:
    print(f"{combination_counter} combinations - neither equals {magic_number}")


