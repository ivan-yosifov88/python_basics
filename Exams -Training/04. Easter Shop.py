start_quantity_eggs = int(input())
total_eggs_sold = 0
command = input()
no_more_eggs = False
while command != "Close":
    new_command = command
    number_of_eggs = int(input())
    if new_command == "Buy":
        if start_quantity_eggs - number_of_eggs < 0:
            no_more_eggs = True
            break
        else:
            start_quantity_eggs -= number_of_eggs
            total_eggs_sold += number_of_eggs

    if new_command == "Fill":
        start_quantity_eggs += number_of_eggs
    command = input()
if no_more_eggs:
    print("Not enough eggs in store!")
    print(f"You can buy only {start_quantity_eggs}.")
else:
    print("Store is closed!")
    print(f"{total_eggs_sold} eggs sold.")
