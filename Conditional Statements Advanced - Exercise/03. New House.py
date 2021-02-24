kind_of_flowers = input()
number_flowers = int(input())
budged = int(input())
price = 0
if kind_of_flowers == "Roses":
    if number_flowers > 80:
        price = number_flowers * 5 * 0.9
    else:
        price = number_flowers * 5
elif kind_of_flowers == "Dahlias":
    if number_flowers > 90:
        price = number_flowers * 3.8 * 0.85
    else:
        price = number_flowers * 3.8
elif kind_of_flowers == "Tulips":
    if number_flowers > 80:
        price = number_flowers * 2.8 * 0.85
    else:
        price = number_flowers * 2.8
elif kind_of_flowers == "Narcissus":
    if number_flowers < 120:
        price = number_flowers * 3 * 1.15
    else:
        price = number_flowers * 3
elif kind_of_flowers == "Gladiolus":
    if number_flowers < 80:
        price = number_flowers * 2.5 * 1.2
    else:
        price = number_flowers * 2.5
difference = abs(budged - price)
if budged >= price:
    print(f"Hey, you have a great garden with {number_flowers} {kind_of_flowers} and {difference:.2f} leva left.")
else:
    print(f"Not enough money, you need {difference:.2f} leva more.")
