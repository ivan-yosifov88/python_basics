# •	Ако дестинацията е Дубай – 30% отстъпка от крайната цена
# •	Ако дестинацията е София – цената се оскъпява с 25%
budget = float(input())
destination = input()
season = input()
number_days = int(input())
price = 0
total_price = 0
if season == "Winter":
    if destination == "Dubai":
        price = 45000
    elif destination == "Sofia":
        price = 17000
    elif destination == "London":
        price = 24000
elif season == "Summer":
    if destination == "Dubai":
        price = 40000
    elif destination == "Sofia":
        price = 12500
    elif destination == "London":
        price = 20250
total_price = number_days * price
if destination == "Dubai":
    total_price *= 0.7
if destination == "Sofia":
    total_price *= 1.25
difference = abs(budget - total_price)
if budget >= total_price:
    print(f"The budget for the movie is enough! We have {difference:.2f} leva left!")
else:
    print(f"The director needs {difference:.2f} leva more!")
