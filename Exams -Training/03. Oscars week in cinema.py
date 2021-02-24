movie_title = input()
type_of_hall = input()
number_of_tickets = int(input())
price = 0
if type_of_hall == "normal":
    if movie_title == "A Star Is Born":
        price = 7.5
    elif movie_title == "Bohemian Rhapsody":
        price = 7.35
    elif movie_title == "Green Book":
        price = 8.15
    elif movie_title == "The Favourite":
        price = 8.75
elif type_of_hall == "luxury":
    if movie_title == "A Star Is Born":
        price = 10.5
    elif movie_title == "Bohemian Rhapsody":
        price = 9.45
    elif movie_title == "Green Book":
        price = 10.25
    elif movie_title == "The Favourite":
        price = 11.55
elif type_of_hall == "ultra luxury":
    if movie_title == "A Star Is Born":
        price = 13.5
    elif movie_title == "Bohemian Rhapsody":
        price = 12.75
    elif movie_title == "Green Book":
        price = 13.25
    elif movie_title == "The Favourite":
        price = 13.95
total_price = price * number_of_tickets
print(f"{movie_title} -> {total_price:.2f} lv.")