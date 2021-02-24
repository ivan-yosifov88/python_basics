command = input()
best_movie = ""
max_sum = 0
movie_number = 0
while command != "STOP":
    total_sum = 0
    movie_title = command
    movie_number += 1
    for index, digit in enumerate(movie_title):
        if 97 <= ord(digit) <= 122:
            total_sum += ord(digit) - 2 * len(movie_title)
        elif 65 <= ord(digit) <= 90:
            total_sum += ord(digit) - len(movie_title)
        elif ord(digit) == 32:
            total_sum += ord(digit)
        elif 48 <= ord(digit) <= 57:
            total_sum += ord(digit)
    if total_sum > max_sum:
        max_sum = total_sum
        best_movie = movie_title
    if movie_number == 7:
        print("The limit is reached.")
        break
    command = input()
print(f"The best movie for you is {best_movie} with {max_sum} ASCII sum.")



