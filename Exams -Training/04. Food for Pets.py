number_of_days = int(input())
total_pet_food = float(input())
total_eaten_biscuits = 0
total_eaten_food_from_dog = 0
total_eaten_food_from_cat = 0
for days in range(1, number_of_days + 1):
    food_eaten_from_dog = int(input())
    food_eaten_from_cat = int(input())
    if days % 3 == 0:
        total_eaten_biscuits += (food_eaten_from_dog + food_eaten_from_cat) * 0.1
    total_eaten_food_from_dog += food_eaten_from_dog
    total_eaten_food_from_cat += food_eaten_from_cat
total_eaten_food = total_eaten_food_from_dog + total_eaten_food_from_cat
percent_total_eaten_food = total_eaten_food / total_pet_food * 100
percent_total_eaten_food_from_dog = total_eaten_food_from_dog / total_eaten_food * 100
percent_total_eaten_food_from_cat = total_eaten_food_from_cat / total_eaten_food * 100
print(f"Total eaten biscuits: {round(total_eaten_biscuits)}gr.")
print(f"{percent_total_eaten_food:.2f}% of the food has been eaten.")
print(f"{percent_total_eaten_food_from_dog:.2f}% eaten from the dog.")
print(f"{percent_total_eaten_food_from_cat:.2f}% eaten from the cat.")
