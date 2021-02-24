import math
number_of_magnolias = int(input())
number_of_hyacinths= int(input())
number_of_roses = int(input())
number_of_cacti = int(input())
price_of_gift = float(input())
total_money = number_of_magnolias * 3.25 + number_of_hyacinths * 4 + number_of_roses * 3.5 + number_of_cacti * 8
total_money *= 0.95
difference = abs(price_of_gift - total_money)
if total_money >= price_of_gift:
    print(f"She is left with {math.floor(difference)} leva.")
else:
    print(f"She will have to borrow {math.ceil(difference)} leva.")

