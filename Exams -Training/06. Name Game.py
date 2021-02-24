command = input()
max_points = 0
winner_name = ""
while command != "Stop":
    player_name = command
    points = 0
    for index, digit in enumerate(player_name):
        new_number = int(input())
        if new_number == ord(digit):
            points += 10
        else:
            points += 2
        if index == len(player_name):
            break
    command = input()
    if max_points <= points:
        max_points = points
        winner_name = player_name
print(f"The winner is {winner_name} with {max_points} points!")