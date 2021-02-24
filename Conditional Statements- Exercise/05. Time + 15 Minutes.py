hours = int(input())
minutes = int(input())
current_time = hours * 60 + minutes
time_after_fifteen_minutes = current_time + 15
hours_after_fifteen = time_after_fifteen_minutes // 60
minutes_after_fifteen = time_after_fifteen_minutes % 60
if hours_after_fifteen > 23:
    hours_after_fifteen -= 24
if minutes_after_fifteen < 10:
    print(f"{hours_after_fifteen}:0{minutes_after_fifteen}")
else:
    print(f"{hours_after_fifteen}:{minutes_after_fifteen}")

