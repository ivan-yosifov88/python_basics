name_of_player_one = input()
name_of_player_two = input()
first_player_wins = 0
second_player_wins = 0
winner = 0
points = 0
is_number_wars = False
command = input()
while command != "End of game":
    first_player_card = int(command)
    second_player_card = int(input())
    if first_player_card > second_player_card:
        first_player_wins += first_player_card - second_player_card
        # first_player_wins += win_first
    elif second_player_card > first_player_card:
        second_player_wins += second_player_card - first_player_card
    else:
        first_player_card = int(input())
        second_player_card = int(input())
        if first_player_card > second_player_card:
            points = first_player_wins
            winner = name_of_player_one
        elif second_player_card > first_player_card:
            points = second_player_wins
            winner = name_of_player_two
        is_number_wars = True
        break
    command = input()
if is_number_wars:
    print("Number wars!")
    print(f"{winner} is winner with {points} points")
else:
    print(f"{name_of_player_one} has {first_player_wins} points")
    print(f"{name_of_player_two} has {second_player_wins} points")

