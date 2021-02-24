holidays =  int(input())
workdays = 365 - holidays
game_for_play = (365 - holidays) * 63 + holidays * 127
norm_to_sleep_well = abs(30000 - game_for_play)
hours_to_sleep = norm_to_sleep_well // 60
minutes_to_sleep = norm_to_sleep_well % 60
if game_for_play > 30000:
    print("Tom will run away")
    print(f"{hours_to_sleep} hours and {minutes_to_sleep} minutes more for play")
elif game_for_play < 30000:
    print("Tom sleeps well")
    print(f"{hours_to_sleep} hours and {minutes_to_sleep} minutes less for play")


