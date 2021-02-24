number_airlines = int(input())
max_passengers = 0
airline_with_max_passengers = ""
for airlines in range(number_airlines):
    total_passengers = 0
    number_of_flights = 0
    name_of_airlines = (input())
    command = input()
    average_number_of_passengers = 0
    while command != "Finish":
        number_of_passengers = int(command)
        total_passengers += number_of_passengers
        number_of_flights += 1
        command = input()
    average_number_of_passengers = int(total_passengers / number_of_flights)
    print(f"{name_of_airlines}: {average_number_of_passengers} passengers.")
    if average_number_of_passengers > max_passengers:
        max_passengers = average_number_of_passengers
        airline_with_max_passengers = name_of_airlines
print(f"{airline_with_max_passengers} has most passengers per flight: {max_passengers}")


