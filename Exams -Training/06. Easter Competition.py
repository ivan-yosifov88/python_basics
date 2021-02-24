import sys

number_of_breads = int(input())
max_score = - sys.maxsize
is_baker_win = False
baker_winner = ""
for breads in range(number_of_breads):
    name_of_baker = input()
    command = input()
    total_score = 0
    while command != "Stop":
        score = int(command)
        total_score += score
        command = input()
    print(f"{name_of_baker} has {total_score} points.")
    if total_score > max_score:
        max_score = total_score
        is_baker_win = True
        baker_winner = name_of_baker
        print(f"{name_of_baker} is the new number 1!")
if is_baker_win:
    print(f"{baker_winner} won competition with {max_score} points!")

