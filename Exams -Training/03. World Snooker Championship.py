championship_stage = input()
type_of_tickets = input()
number_of_tickets = int(input())
photo_with_trophy = input()
price = 0
total_price = 0
price_of_foto = 40
if championship_stage == "Quarter final":
    if type_of_tickets == "Standard":
        price = 55.5
    elif type_of_tickets == "Premium":
        price = 105.2
    elif type_of_tickets == "VIP":
        price = 118.9
elif championship_stage == "Semi final":
    if type_of_tickets == "Standard":
        price = 75.88
    elif type_of_tickets == "Premium":
        price = 125.22
    elif type_of_tickets == "VIP":
        price = 300.4
elif championship_stage == "Final":
    if type_of_tickets == "Standard":
        price =110.1
    elif type_of_tickets == "Premium":
        price = 160.66
    elif type_of_tickets == "VIP":
        price = 400
total_price = price * number_of_tickets
if 2500 < total_price <= 4000:
    total_price *= 0.9
if total_price > 4000:
    total_price *= 0.75
if photo_with_trophy == "Y" and total_price <= 4000:
    total_price += price_of_foto * number_of_tickets
print(f"{total_price:.2f}")