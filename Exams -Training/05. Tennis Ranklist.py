number_of_tournaments = int(input())
points_in_rank_list = int(input())
final_points = points_in_rank_list
total_points = 0
number_of_wins = 0
for tournaments in range(number_of_tournaments):
    stage_of_tournament = input()
    if stage_of_tournament == "W":
        number_of_wins += 1
        total_points += 2000
    elif stage_of_tournament == "F":
        total_points += 1200
    elif stage_of_tournament == "SF":
        total_points += 720
final_points += total_points
average_points = total_points/ number_of_tournaments
percent_win_tournaments = number_of_wins / number_of_tournaments * 100
print(f"Final points: {final_points}")
print(f"Average points: {int(average_points)}")
print(f"{percent_win_tournaments:.2f}%")