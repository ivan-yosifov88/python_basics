number_junior_bikers = int(input())
number_senior_bikers = int(input())
type_of_road = input()
all_tax = 0
if type_of_road == "trail":
   all_tax = 5.5 * number_junior_bikers + 7 * number_senior_bikers
elif type_of_road == "cross-country":
    all_tax = 8 * number_junior_bikers + 9.5 * number_senior_bikers
elif type_of_road == "downhill":
    all_tax = 12.25 * number_junior_bikers + 13.75 * number_senior_bikers
elif type_of_road == "road":
    all_tax = 20 * number_junior_bikers + 21.5 * number_senior_bikers
if type_of_road == "cross-country" and (number_senior_bikers + number_junior_bikers) >= 50:
    all_tax *= 0.75
costs = all_tax * 0.05
print(f"{(all_tax - costs):.2f}")