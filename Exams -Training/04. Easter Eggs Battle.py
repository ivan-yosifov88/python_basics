# Ако първият играч остане без яйца:
# •	"Player one is out of eggs. Player two has {брой останали яйца на втория играч} eggs left."
# Ако вторият играч остане без яйца:
# •	"Player two is out of eggs. Player one has {брой останали яйца на първия играч} eggs left."
# При команда "End of battle" да се отпечатат два реда:
# •	"Player one has {брой останали яйца на първия играч} eggs left."
# •	"Player two has {брой останали яйца на втория играч} eggs left."

number_of_eggs_first_player = int(input())
number_of_eggs_second_player = int(input())
command = input()
first_player_out_of_eggs = False
second_player_out_of_eggs = False
while command != "End of battle":
    winner = command
    if winner == "one":
        number_of_eggs_second_player -= 1
        if number_of_eggs_second_player == 0:
            second_player_out_of_eggs = True
            break
    elif winner == "two":
        number_of_eggs_first_player -= 1
        if number_of_eggs_first_player == 0:
            first_player_out_of_eggs = True
            break
    command = input()
if first_player_out_of_eggs:
    print(f"Player one is out of eggs. Player two has {number_of_eggs_second_player} eggs left.")
elif second_player_out_of_eggs:
    print(f"Player two is out of eggs. Player one has {number_of_eggs_first_player} eggs left.")
else:
    print(f"Player one has {number_of_eggs_first_player} eggs left.")
    print(f"Player two has {number_of_eggs_second_player} eggs left.")