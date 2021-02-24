budget = float(input())
number_of_nights = int(input())
price_for_night = float(input())
percent_other_costs = int(input())
if number_of_nights > 7:
    price_for_night *= 0.95
total_money = number_of_nights * price_for_night + budget * percent_other_costs / 100
difference = abs(budget - total_money)
if total_money <= budget:
    print(f"Ivanovi will be left with {difference:.2f} leva after vacation.")
else:
    print(f"{difference:.2f} leva needed.")