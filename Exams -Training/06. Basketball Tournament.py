command = input()
win_counter = 0
loss_counter = 0
total_games = 0
while command != "End of tournaments":
    name_of_tournament = command
    number_of_games = int(input())
    difference = 0
    for games in range(1, number_of_games + 1):
        points_our_team = int(input())
        points_opposing_team = int(input())
        difference = abs(points_our_team - points_opposing_team)
        total_games += 1
        if points_our_team > points_opposing_team:
            win_counter += 1
            print(f"Game {games} of tournament {name_of_tournament}: win with {difference} points.")
        elif points_our_team < points_opposing_team:
            loss_counter += 1
            print(f"Game {games} of tournament {name_of_tournament}: lost with {difference} points.")
    command = input()
percent_win = win_counter / total_games * 100
percent_loss = loss_counter / total_games * 100
print(f"{percent_win:.2f}% matches win")
print(f"{percent_loss:.2f}% matches lost")




