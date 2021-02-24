airplane_cargo_capacity = float(input())
command = input()
total_suitcase_volume = 0
number_of_suitcase_loaded = 0
is_cargo_full = False
while command != "End":
    suitcase_volume = float(command)
    if number_of_suitcase_loaded % 3 == 0:
        suitcase_volume * 1.1
    total_suitcase_volume += suitcase_volume
    if airplane_cargo_capacity <= total_suitcase_volume:
        is_cargo_full = True
        break
    number_of_suitcase_loaded += 1
    command = input()
if is_cargo_full:
    print("No more space!")
else:
    print("Congratulations! All suitcases are loaded!")
print(f"Statistic: {number_of_suitcase_loaded} suitcases loaded.")





