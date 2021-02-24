budget = float(input())
command = input()
total_price_of_products = 0
number_of_products = 0
is_money_spent = False
while command != "Stop":
    name_of_product = command
    price_of_product = float(input())
    number_of_products += 1
    if number_of_products % 3 == 0:
        price_of_product *= 0.5
    total_price_of_products += price_of_product
    if budget < total_price_of_products:
        difference = abs(budget - total_price_of_products)
        is_money_spent = True
        break
    command = input()
if is_money_spent:
    print("You don't have enough money!")
    print(f"You need {difference:.2f} leva!")
else:
    print(f"You bought {number_of_products} products for {total_price_of_products:.2f} leva.")
