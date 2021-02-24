dog_food = int(input())
dog_food_in_grams = dog_food * 1000
command = input()
is_dog_food_enough = True
while command != "Adopted":
    dog_meal = int(command)
    dog_food_in_grams -= dog_meal
    if dog_food_in_grams < 0:
        is_dog_food_enough = False

    command = input()
if is_dog_food_enough:
    print(f"Food is enough! Leftovers: {dog_food_in_grams} grams.")
else:
    print(f"Food is not enough. You need {abs(dog_food_in_grams)} grams more.")
