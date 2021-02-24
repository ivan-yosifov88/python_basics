desired_profit = float(input())
current_profit = 0
command = input()
while command != "Party!":
    cocktail_name = command
    number_of_cocktail = int(input())
    cocktail_price = len(cocktail_name)
    order_price = cocktail_price * number_of_cocktail
    if order_price % 2 == 1:
        order_price *= 0.75
    current_profit += order_price
    if current_profit >= desired_profit:
        break

    command = input()
difference = abs(current_profit - desired_profit)
if command == "Party!":
    print(f"We need {difference:.2f} leva more.")
else:
    print("Target acquired.")
print(f"Club income - {current_profit:.2f} leva.")