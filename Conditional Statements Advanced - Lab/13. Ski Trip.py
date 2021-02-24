days_stay = int(input())
type_of_room = input()
rate = input()
nights = days_stay - 1
price = 0
if nights < 10:
    if type_of_room == "room for one person":
        price = 18
    elif type_of_room == "apartment":
        price = 25 * 0.7
    elif type_of_room == "president apartment":
        price = 35 * 0.9
elif 10 <= nights <= 15:
    if type_of_room == "room for one person":
        price = 18
    elif type_of_room == "apartment":
        price = 25 * 0.65
    elif type_of_room == "president apartment":
        price = 35 * 0.85
elif nights > 15:
    if type_of_room == "room for one person":
        price = 18
    elif type_of_room == "apartment":
        price = 25 * 0.5
    elif type_of_room == "president apartment":
        price = 35 * 0.8
if rate == "positive":
    price *= 1.25
elif rate == "negative":
    price *= 0.9
print(f"{(nights * price):.2f}")




