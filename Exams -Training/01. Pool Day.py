from math import ceil
number_of_people = int(input())
entrance_price = float(input())
price_of_deck_chair = float(input())
price_of_umbrella = float(input())
number_of_deck_chairs = ceil(number_of_people * 0.75)
number_of_umbrellas = ceil(number_of_people / 2)
needed_money = number_of_people * entrance_price + price_of_deck_chair * number_of_deck_chairs + price_of_umbrella * number_of_umbrellas
print(f"{needed_money:.2f} lv.")
