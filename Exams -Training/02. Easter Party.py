number_of_guests = int(input())
price_of_the_envelop = float(input())
budget = float(input())
cake_price = budget * 0.1
new_price = 0
if 10 <= number_of_guests <= 15:
    new_price = price_of_the_envelop * 0.85
elif 15 < number_of_guests <= 20:
    new_price = price_of_the_envelop * 0.80
elif number_of_guests > 20:
    new_price = price_of_the_envelop * 0.75
else:
    new_price = price_of_the_envelop
needed_money = cake_price + new_price * number_of_guests
difference = abs(budget - needed_money)
if budget >= needed_money:
    print(f"It is party time! {difference:.2f} leva left.")
else:
    print(f"No party! {difference:.2f} leva needed.")