command = input()
people_under_sixteen = 0
people_over_sixteen = 0
while command != "Christmas":
    age = int(command)
    if age <= 16:
        people_under_sixteen += 1
    elif age > 16:
        people_over_sixteen += 1
    command = input()
total_sum_sweaters = people_over_sixteen * 15
total_sum_toys = people_under_sixteen * 5
print(f"Number of adults: {people_over_sixteen}" )
print(f"Number of kids: {people_under_sixteen}")
print(f"Money for toys: {total_sum_toys}")
print(f"Money for sweaters: {total_sum_sweaters}")
