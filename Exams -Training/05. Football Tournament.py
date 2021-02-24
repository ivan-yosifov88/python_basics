football_team = input()
football_matches = int(input())
number_wins = 0
number_equal = 0
number_loss = 0
points = 0
for matches in range(football_matches):
    if football_matches == 0:
        break
    else:
        result_of_the_match = input()
        if result_of_the_match == "W":
            number_wins += 1
            points += 3
        elif result_of_the_match == "D":
            number_equal += 1
            points += 1
        elif result_of_the_match == "L":
            number_loss += 1
if football_matches == 0:
    print(f"{football_team} hasn't played any games during this season.")
else:
    percent_win_points = number_wins / football_matches * 100
    print(f"{football_team} has won {points} points during this season.")
    print("Total stats:")
    print(f"## W: {number_wins}")
    print(f"## D: {number_equal}")
    print(f"## L: {number_loss}")
    print(f"Win rate: {percent_win_points:.2f}%")
