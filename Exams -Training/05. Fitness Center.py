fitness_visitors = int(input())
number_of_people_train_back = 0
number_of_people_train_chest = 0
number_of_people_train_legs = 0
number_of_people_train_abs = 0
number_of_people_buy_shake = 0
number_of_people_buy_bar = 0
trainers = 0
protein_buyers = 0
for visitors in range(fitness_visitors):
    fitness_activity = input()
    if fitness_activity == "Back":
        number_of_people_train_back += 1
        trainers += 1
    elif fitness_activity == "Chest":
        number_of_people_train_chest += 1
        trainers += 1
    elif fitness_activity == "Legs":
        number_of_people_train_legs += 1
        trainers += 1
    elif fitness_activity == "Abs":
        number_of_people_train_abs += 1
        trainers += 1
    elif fitness_activity == "Protein shake":
        number_of_people_buy_shake += 1
        protein_buyers += 1
    elif fitness_activity == "Protein bar":
        number_of_people_buy_bar += 1
        protein_buyers += 1
percent_trainers = trainers / fitness_visitors * 100
percent_protein_buyers = protein_buyers / fitness_visitors * 100
print(f"{number_of_people_train_back} - back")
print(f"{number_of_people_train_chest} - chest")
print(f"{number_of_people_train_legs} - legs")
print(f"{number_of_people_train_abs} - abs")
print(f"{number_of_people_buy_shake} - protein shake")
print(f"{number_of_people_buy_bar} - protein bar")
print(f"{percent_trainers:.2f}% - work out")
print(f"{percent_protein_buyers:.2f}% - protein")


