budget = float(input())
needed_fuel = float(input())
day_of_week = input()
price_fuel = needed_fuel * 2.1
price_of_guide = 100
sum_of_safari = price_fuel + price_of_guide
if day_of_week == "Saturday":
    sum_of_safari *= 0.90
elif day_of_week == "Sunday":
    sum_of_safari *= 0.80
difference = abs(budget - sum_of_safari)
if budget >= sum_of_safari:
    print(f"Safari time! Money left: {difference:.2f} lv. ")
else:
    print(f"Not enough money! Money needed: {difference:.2f} lv.")