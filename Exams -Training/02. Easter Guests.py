from math import ceil
number_of_guests = int(input())
budget = int(input())
number_of_eggs = number_of_guests * 2
number_of_easter_cakes = ceil(number_of_guests / 3)
price_of_all_eggs = number_of_eggs * 0.45
price_of_all_easter_cakes = number_of_easter_cakes * 4
total_sum = price_of_all_easter_cakes + price_of_all_eggs
difference = abs(budget - total_sum)
if budget >= total_sum:
    print(f"Lyubo bought {number_of_easter_cakes} Easter bread and {number_of_eggs} eggs.")
    print(f"He has {difference:.2f} lv. left.")
else:
    print("Lyubo doesn't have enough money.")
    print(f"He needs {difference:.2f} lv. more.")