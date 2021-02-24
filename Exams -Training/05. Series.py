budget = float(input())
number_of_series = int(input())
total_price = 0
for series in range(number_of_series):
    title = input()
    price = float(input())
    if title == "Thrones":
        price *= 0.5
    elif title == "Lucifer":
        price *= 0.6
    elif title == "Protector":
        price *= 0.7
    elif title == "TotalDrama":
        price *= 0.8
    elif title == "Area":
        price *= 0.9
    total_price += price
difference = abs(budget - total_price)
if budget >= total_price:
    print(f"You bought all the series and left with {difference:.2f} lv.")
else:
    print(f"You need {difference:.2f} lv. more to buy the series!")
