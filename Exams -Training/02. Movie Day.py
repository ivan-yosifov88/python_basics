time_of_movie = int(input())
number_of_scenes = int(input())
time_of_scene = int(input())
total_time = number_of_scenes * time_of_scene + time_of_movie * 0.15
difference = abs(time_of_movie - total_time)
if total_time <= time_of_movie:
    print(f"You managed to finish the movie on time! You have {round(difference)} minutes left!")
else:
    print(f"Time is up! To complete the movie you need {round(difference)} minutes.")