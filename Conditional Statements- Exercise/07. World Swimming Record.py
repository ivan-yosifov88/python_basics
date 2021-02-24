record_in_seconds = float(input())
distance_in_meters = float(input())
time_in_seconds_for_one_meter = float(input())
ivan_time = distance_in_meters * time_in_seconds_for_one_meter
resistance_in_seconds = int(distance_in_meters / 15) * 12.5
ivan_total_time = ivan_time + resistance_in_seconds
difference = abs(record_in_seconds - ivan_total_time)
if record_in_seconds > ivan_total_time:
    print(f"Yes, he succeeded! The new world record is {ivan_total_time:.2f} seconds.")
else:
    print(f"No, he failed! He was {difference:.2f} seconds slower.")