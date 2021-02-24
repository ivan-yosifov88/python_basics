name_of_series = input()
number_of_seasons = int(input())
number_of_episodes = int(input())
time_of_series_without_ad = float(input())
special_episodes = number_of_seasons * 10
time_of_episodes = time_of_series_without_ad * 1.2
total_time = number_of_seasons * number_of_episodes * time_of_episodes + special_episodes
print(f"Total time needed to watch the {name_of_series} series is {int(total_time)} minutes.")