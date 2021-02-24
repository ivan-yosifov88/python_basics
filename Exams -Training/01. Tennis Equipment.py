from math import ceil, floor
price_of_tennis_racket = float(input())
number_of_tennis_racket = int(input())
number_of_sneakers = int(input())
price_sneakers = price_of_tennis_racket / 6
price_of_equipment = price_of_tennis_racket * number_of_tennis_racket + price_sneakers * number_of_sneakers
price_of_other_equipment = price_of_equipment * 0.20
total_sum = price_of_equipment + price_of_other_equipment
tennis_player = floor(total_sum / 8)
sponsors = ceil(total_sum * 7 / 8)
print(f"Price to be paid by Djokovic {tennis_player}")
print(f"Price to be paid by sponsors {sponsors}")
