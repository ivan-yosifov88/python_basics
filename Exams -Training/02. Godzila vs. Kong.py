budget = float(input())
number_of_extras = int(input())
price_of_clothing_for_one = float(input())
decor_price = budget * 0.1
if number_of_extras > 150:
    price_of_clothing_for_one *= 0.9
needed_money = number_of_extras * price_of_clothing_for_one + decor_price
difference = abs(budget - needed_money)
if needed_money > budget:
    print("Not enough money!")
    print(f"Wingard needs {difference:.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {difference:.2f} leva left.")


