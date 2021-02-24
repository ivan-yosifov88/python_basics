size_of_eggs = input()
eggs_colour = input()
batch_of_eggs = int(input())
price = 0
final_price = 0
if size_of_eggs == "Large":
    if eggs_colour == "Red":
        price = 16
    elif eggs_colour == "Green":
        price = 12
    elif eggs_colour == "Yellow":
        price = 9
elif size_of_eggs == "Medium":
    if eggs_colour == "Red":
        price = 13
    elif eggs_colour == "Green":
        price = 9
    elif eggs_colour == "Yellow":
        price = 7
elif size_of_eggs == "Small":
    if eggs_colour == "Red":
        price = 9
    elif eggs_colour == "Green":
        price = 8
    elif eggs_colour == "Yellow":
        price = 5
final_price = batch_of_eggs * price
final_price *= 0.65
print(f"{final_price:.2f} leva.")


