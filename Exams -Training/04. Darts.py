name_of_player = input()
command = input()
total_points = 301
current_points = 0
valid_shots = 0
invalid_shots = 0
is_player_win = False
while not command == "Retire":
    field = command
    points = int(input())
    if field == "Triple":
        points *= 3
    elif field == "Double":
        points *= 2
    elif field == "Single":
        points
    current_points += points
    if total_points >= current_points:
        valid_shots += 1
        total_points -= current_points
        if total_points == 0 :
            is_player_win = True
            break
    elif total_points < current_points:
        invalid_shots += 1
    current_points = 0
    command = input()
if is_player_win:
    print(f"{name_of_player} won the leg with {valid_shots} shots.")
else:
    print(f"{name_of_player} retired after {invalid_shots} unsuccessful shots.")

