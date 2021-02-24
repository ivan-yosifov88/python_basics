destination = input()
date_of_reservation = input()
number_nights = int(input())
price = 0
vacation_cost = 0
if destination == "France":
    if date_of_reservation == "21-23":
        price = 30
    elif date_of_reservation == "24-27":
        price = 35
    elif date_of_reservation == "28-31":
        price = 40
elif destination == "Italy":
    if date_of_reservation == "21-23":
        price = 28
    elif date_of_reservation == "24-27":
        price = 32
    elif date_of_reservation == "28-31":
        price = 39
elif destination == "Germany":
    if date_of_reservation == "21-23":
        price = 32
    elif date_of_reservation == "24-27":
        price = 37
    elif date_of_reservation == "28-31":
        price = 43
vacation_cost = number_nights * price
print(f"Easter trip to {destination} : {vacation_cost:.2f} leva.")
