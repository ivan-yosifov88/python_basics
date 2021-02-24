budget = float(input())
category = input()
number_of_peoples = int(input())
transport_price  = 0
total_money = 0
if 1 <= number_of_peoples <= 4:
    transport_price = budget * 0.75
elif 5 <= number_of_peoples <= 9:
    transport_price = budget * 0.60
elif 10 <= number_of_peoples <= 24:
    transport_price = budget * 0.50
elif 25 <= number_of_peoples <= 49:
    transport_price = budget * 0.40
elif number_of_peoples >= 50:
    transport_price = budget * 0.25
if category == "VIP":
    total_money = number_of_peoples * 499.99 + transport_price
elif category == "Normal":
    total_money = number_of_peoples * 249.99 + transport_price
difference = abs(budget - total_money)
if budget >= total_money:
    print(f"Yes! You have {difference:.2f} leva left.")
else:
    print(f"Not enough money! You need {difference:.2f} leva.")