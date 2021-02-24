import math

average_speed = float(input())
fuel_for_hundred_kilometers = float(input())
distance = 384400
time_stay = 3
total_distance = distance * 2
total_time = total_distance / average_speed + time_stay
fuel_consumption = fuel_for_hundred_kilometers * total_distance / 100
print(math.ceil(total_time))
print(int(fuel_consumption))