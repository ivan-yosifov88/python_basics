name_of_film = input()
number_of_days = int(input())
number_of_tickets = int(input())
price_of_ticket = float(input())
percent_for_cinema = int(input())
total_sum = number_of_days * number_of_tickets * price_of_ticket * (100 - percent_for_cinema ) / 100
print(f"The profit from the movie {name_of_film} is {total_sum:.2f} lv.")