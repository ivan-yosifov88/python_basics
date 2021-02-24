from math import floor, ceil
number_of_days = int(input())
left_food = int(input())
dog_food = float(input())
cat_food = float(input())
turtle_food = float(input())
kilogram_food_eaten = number_of_days * (dog_food + cat_food + turtle_food / 1000)
difference = abs(left_food - kilogram_food_eaten)
if left_food >= kilogram_food_eaten:
    print(f"{floor(difference)} kilos of food left.")
else:
    print(f"{ceil(difference)} more kilos of food are needed.")

