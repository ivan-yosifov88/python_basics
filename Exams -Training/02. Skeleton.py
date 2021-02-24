# Ред 1.	Минути на контролата – цяло число в интервала [0…59]
# Ред 2.	Секунди на контролата – цяло число в интервала [0…59]
# Ред 3.	Дължината на улея в метри – реално число в интервала [0.00…50000]
# Ред 4.	Секунди за изминаване на 100 метра – цяло число в интервала [0…1000]
minutes = int(input())
seconds = int(input())
length_in_meters = float(input())
seconds_for_hundred_meter = int(input())
time_to_beat = minutes * 60 + seconds
time_of_racer = length_in_meters / 100 * seconds_for_hundred_meter
total_time = time_of_racer - length_in_meters / 120 * 2.5
difference = abs(time_to_beat - total_time)
if total_time <= time_to_beat:
    print("Marin Bangiev won an Olympic quota!")
    print(f"His time is {total_time:.3f}.")
else:
    print(f"No, Marin failed! He was {difference:.3f} second slower.")