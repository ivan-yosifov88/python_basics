# •	Ако сумата е достатъчна:
# "You purchased a 1 month pass for {sport}."
# където {sport} е въведения тип спорт
# •	Ако сумата не е достатъчна трябва да се пресметне колко още пари са необходими, за да се закупи карта:
# "You don't have enough money! You need ${money} more."
# където {money} e оставащата сума нужна, за да се закупи картата, форматирана до втория знак след десетичната запетая.

money_on_hand = float(input())
gender = input()
age = int(input())
type_of_sport = input()
fitness_card = 0
if gender == "m":
    if type_of_sport == "Gym":
        fitness_card = 42
    elif type_of_sport == "Boxing":
        fitness_card = 41
    elif type_of_sport == "Yoga":
        fitness_card = 45
    elif type_of_sport == "Zumba":
        fitness_card = 34
    elif type_of_sport == "Dances":
        fitness_card = 51
    elif type_of_sport == "Pilates":
        fitness_card = 39
elif gender == "f":
    if type_of_sport == "Gym":
        fitness_card = 35
    elif type_of_sport == "Boxing":
        fitness_card = 37
    elif type_of_sport == "Yoga":
        fitness_card = 42
    elif type_of_sport == "Zumba":
        fitness_card = 31
    elif type_of_sport == "Dances":
        fitness_card = 53
    elif type_of_sport == "Pilates":
        fitness_card = 37
if age <= 19:
    fitness_card *= 0.8
difference = abs(money_on_hand - fitness_card)
if money_on_hand >= fitness_card:
    print(f"You purchased a 1 month pass for {type_of_sport}.")
else:
    print(f"You don't have enough money! You need ${difference:.2f} more.")

