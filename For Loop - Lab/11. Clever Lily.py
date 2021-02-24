ages = int(input())
price_of_laundry = float(input())
price_per_toy = float(input())
birthday_money = 0
total_money = 0
total_toys = 0
for age in range(1, ages +1):
    if age % 2 == 0:
        birthday_money += 10
        total_money += birthday_money - 1
    else:
        total_toys += 1
total_money += total_toys * price_per_toy
difference = abs(total_money - price_of_laundry)
if total_money >= price_of_laundry:
    print(f"Yes! {difference:.2f}")
else:
    print(f"No! {difference:.2f}")
