number_of_kilometers = int(input())
day_or_night = input()
price = 0
if number_of_kilometers < 20:
    if day_or_night == "day":
        price = 0.70 + 0.79 * number_of_kilometers
    elif day_or_night == "night":
        price = 0.7 + 0.9 * number_of_kilometers
elif 20 <= number_of_kilometers < 100:
    price = 0.09 * number_of_kilometers
elif number_of_kilometers >= 100:
    price = 0.06 * number_of_kilometers
print(f"{price:.2f}")