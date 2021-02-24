number_sell_games = int(input())
sell_hearthstone = 0
sell_fornite = 0
sell_overwatch = 0
sell_others = 0
total_sells = 0
for games in range(number_sell_games):
    game_name = input()
    total_sells += 1
    if game_name == "Hearthstone":
        sell_hearthstone += 1
    elif game_name == "Fornite":
        sell_fornite += 1
    elif game_name == "Overwatch":
        sell_overwatch += 1
    else:
        sell_others += 1
percent_hearthstone = sell_hearthstone / total_sells * 100
percent_fornite = sell_fornite / total_sells * 100
percent_overwatch = sell_overwatch / total_sells * 100
percent_others = sell_others / total_sells * 100
print(f"Hearthstone - {percent_hearthstone:.2f}%")
print(f"Fornite - {percent_fornite:.2f}%")
print(f"Overwatch - {percent_overwatch:.2f}%")
print(f"Others - {percent_others:.2f}%")
