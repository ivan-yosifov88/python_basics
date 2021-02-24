from math import ceil
name_of_series = input()
duration_of_episode = int(input())
duration_of_lunch_break = int(input())
total_time = duration_of_lunch_break - (duration_of_lunch_break / 8 + duration_of_lunch_break / 4)
difference = abs(total_time - duration_of_episode)
if total_time >= duration_of_episode:
    print(f"You have enough time to watch {name_of_series} and left with {ceil(difference)} minutes free time.")
else:
    print(f"You don't have enough time to watch {name_of_series}, you need {ceil(difference)} more minutes.")