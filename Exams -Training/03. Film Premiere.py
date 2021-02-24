movie_name = input()
film_package = input()
number_tickets = int(input())
price = 0
total_price = 0
if movie_name == "John Wick":
    if film_package == "Drink":
        price = 12
    elif film_package == "Popcorn":
        price = 15
    elif film_package == "Menu":
        price = 19
elif movie_name == "Star Wars":
    if film_package == "Drink":
        price = 18
    elif film_package == "Popcorn":
        price = 25
    elif film_package == "Menu":
        price = 30
elif movie_name == "Jumanji":
    if film_package == "Drink":
        price = 9
    elif film_package == "Popcorn":
        price = 11
    elif film_package == "Menu":
        price = 14
total_price = number_tickets * price
if movie_name == "Star Wars" and number_tickets >= 4:
    total_price *= 0.7
if movie_name == "Jumanji" and number_tickets == 2:
    total_price *= 0.85
print(f"Your bill is {total_price:.2f} leva.")