type_of_drink = input()
sweet_type = input()
number_drinks = int(input())
price = 0
total_price = 0
if type_of_drink == "Espresso":
    if sweet_type == "Without":
        price = 0.9
    elif sweet_type == "Normal":
        price = 1
    elif sweet_type == "Extra":
        price = 1.2
elif type_of_drink == "Cappuccino":
    if sweet_type == "Without":
        price = 1
    elif sweet_type == "Normal":
        price = 1.2
    elif sweet_type == "Extra":
        price = 1.6
elif type_of_drink == "Tea":
    if sweet_type == "Without":
        price = 0.5
    elif sweet_type == "Normal":
        price = 0.6
    elif sweet_type == "Extra":
        price = 0.7
total_price = number_drinks * price
if sweet_type == "Without":
    total_price *= 0.65
if type_of_drink == "Espresso" and number_drinks >= 5:
    total_price *= 0.75
if total_price > 15:
    total_price *= 0.8
print(f"You bought {number_drinks} cups of {type_of_drink} for {total_price:.2f} lv.")