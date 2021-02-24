detergent = int(input())
total_detergent = detergent * 750
command = input()
dishwasher_counter = 0
detergent_over = False
sum_plates = 0
sum_pots = 0
while not command == "End":
    number_of_dishes = int(command)
    dishwasher_counter += 1
    if dishwasher_counter < 3:
        sum_plates += number_of_dishes
        total_detergent -= number_of_dishes * 5
    elif dishwasher_counter == 3:
        total_detergent -= number_of_dishes * 15
        sum_pots += number_of_dishes
        dishwasher_counter = 0
    if total_detergent < 0:
        detergent_over = True
        break
    command = input()
if detergent_over:
    print(f"Not enough detergent, {abs(total_detergent)} ml. more necessary!")
else:
    print("Detergent was enough!")
    print(f"{sum_plates} dishes and {sum_pots} pots were washed.")
    print(f"Leftover detergent {total_detergent} ml.")
