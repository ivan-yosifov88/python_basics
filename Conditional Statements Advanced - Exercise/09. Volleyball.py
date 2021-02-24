# •	Първият ред съдържа думата "leap" (високосна година) или "normal" (невисокосна);
# •	Вторият ред съдържа цялото число p – брой празници в годината (които не са събота и неделя);
# •	Третият ред съдържа цялото число h – брой уикенди, в които Влади си пътува до родния град.
type_year = input()
number_holidays = int(input())
number_weekends_in_home_town = int(input())
saturday_play = (48 - number_weekends_in_home_town) * 3 / 4
number_of_holidays_for_play = number_holidays * 2 / 3
times_to_play = saturday_play + number_weekends_in_home_town + number_of_holidays_for_play
if type_year == "leap":
    times_to_play *= 1.15
    print(int(times_to_play))
else:
    print(int(times_to_play))