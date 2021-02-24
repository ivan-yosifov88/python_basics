import sys
number_of_films = int(input())
max_rating = 0
movie_with_max_rating = ""
min_rating = sys.maxsize
movie_with_min_rating = ""
total_sum = 0
for films in range(number_of_films):
    movie_title = input()
    rating = float(input())
    total_sum += rating
    if rating > max_rating:
        max_rating = rating
        movie_with_max_rating = movie_title
    if rating < min_rating:
        min_rating = rating
        movie_with_min_rating = movie_title
average_rating = total_sum / number_of_films
print(f"{movie_with_max_rating} is with highest rating: {max_rating:.1f}")
print(f"{movie_with_min_rating} is with lowest rating: {min_rating:.1f}")
print(f"Average rating: {average_rating:.1f}")
