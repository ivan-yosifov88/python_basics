film_budget = float(input())
# Статист
number_of_extras = int(input())
price_of_clothes = float(input())
price_of_decor = film_budget * 0.1
if number_of_extras > 150:
    price_of_clothes *= 0.9
needed_money = film_budget - (number_of_extras * price_of_clothes) - price_of_decor
if needed_money < 0:
    print("Not enough money!")
    print(f"Wingard needs {abs(needed_money):.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {abs(needed_money):.2f} leva left.")