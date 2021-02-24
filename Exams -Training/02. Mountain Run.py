record_in_seconds = float(input())
distance_in_meters = float(input())
speed_in_seconds_in_meter = float(input())
# Това е важно, защото иначе изхода е грешен
time_delay = int(distance_in_meters / 50) * 30
new_time = distance_in_meters * speed_in_seconds_in_meter
total_time = new_time + time_delay
difference = abs(record_in_seconds - total_time)
if total_time < record_in_seconds:
    print(f"Yes! The new record is {total_time:.2f} seconds.")
else:
    print(f"No! He was {difference:.2f} seconds slower.")
