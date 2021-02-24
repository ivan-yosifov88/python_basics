number_of_coins_one_lev = int(input())
number_of_coins_two_lev = int(input())
number_of_banknotes_five_lev = int(input())
sum_on_hand = int(input())
for one_lev in range(number_of_coins_one_lev + 1):
    for two_lev in range(number_of_coins_two_lev + 1):
        for five_lev in range(number_of_banknotes_five_lev + 1):
            if sum_on_hand == (one_lev * 1 + two_lev * 2 + five_lev * 5):
                print(f"{one_lev} * 1 lv. + {two_lev} * 2 lv. + {five_lev} * 5 lv. = {sum_on_hand} lv.")