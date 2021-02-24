minutes_walk = int(input())
number_of_walks = int(input())
calories_taken = int(input())
burn_calories = minutes_walk * 5 * number_of_walks
if burn_calories >= calories_taken / 2:
    print(f"Yes, the walk for your cat is enough. Burned calories per day: {burn_calories}.")
else:
    print(f"No, the walk for your cat is not enough. Burned calories per day: {burn_calories}.")