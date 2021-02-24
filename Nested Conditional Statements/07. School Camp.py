season = input()
type_of_group = input()
number_students = int(input())
number_of_nights = int(input())
price = 0
type_of_sport = ""
if season == "Winter":
    if type_of_group == "boys":
        type_of_sport = "Judo"
        price = 9.6 * number_students * number_of_nights
    elif type_of_group == "girls":
        type_of_sport = "Gymnastics"
        price = 9.6 * number_students * number_of_nights
    elif type_of_group == "mixed":
        type_of_sport = "Ski"
        price = 10 * number_students * number_of_nights
elif season == "Spring":
    if type_of_group == "boys":
        type_of_sport = "Tennis"
        price = 7.2 * number_students * number_of_nights
    elif type_of_group == "girls":
        type_of_sport = "Athletics"
        price = 7.2 * number_students * number_of_nights
    elif type_of_group == "mixed":
        type_of_sport = "Cycling"
        price = 9.5 * number_students * number_of_nights
elif season == "Summer":
    if type_of_group == "boys":
        type_of_sport = "Football"
        price = 15 * number_students * number_of_nights
    elif type_of_group == "girls":
        type_of_sport = "Volleyball"
        price = 15 * number_students * number_of_nights
    elif type_of_group == "mixed":
        type_of_sport = "Swimming"
        price = 20 * number_students * number_of_nights
if number_students >= 50:
    price *= 0.5
elif 20 <= number_students < 50:
    price *= 0.85
elif 10 <= number_students < 20:
    price *= 0.95
print(f"{type_of_sport} {price:.2f} lv.")

