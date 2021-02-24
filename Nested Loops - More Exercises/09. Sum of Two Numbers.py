start_number = int(input())
end_number = int(input())
magic_number = int(input())
is_combination_magic = False
number_of_combinations = 0
for first_combinations in range(start_number, end_number + 1):
    for second_combinations in range(start_number, end_number + 1):
        number_of_combinations += 1
        if magic_number == first_combinations + second_combinations:
            is_combination_magic = True
            print(f"Combination N:{number_of_combinations} ({first_combinations} + {second_combinations} = {magic_number})")
            break
    if is_combination_magic:
        break
if not is_combination_magic:
    print(f"{number_of_combinations} combinations - neither equals {magic_number}")