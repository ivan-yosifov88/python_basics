number_of_days_for_tournament = int(input())
number_of_wins_in_days = 0
number_of_loses_in_days = 0
total_money = 0
for days in range(number_of_days_for_tournament):
    number_of_wins = 0
    number_of_lose = 0
    total_money_for_day = 0
    command = input()
    while command != "Finish":
        type_of_sport = command
        score = input()
        if score == "win":
            number_of_wins += 1
            total_money_for_day += 20
        elif score == "lose":
            number_of_lose += 1
        command = input()
    if number_of_wins > number_of_lose:
        number_of_wins_in_days += 1
        total_money_for_day *= 1.1
    else:
        number_of_loses_in_days += 1
    total_money += total_money_for_day
if number_of_wins_in_days > number_of_loses_in_days:
    total_money *= 1.2
    print(f"You won the tournament! Total raised money: {total_money:.2f}")
else:
    print(f"You lost the tournament! Total raised money: {total_money:.2f}")


