budget = float(input())
video_cards = int(input())
processors = int(input())
ram_memory = int(input())
video_cards_price = 250
processors_price = video_cards * video_cards_price * 0.35
ram_memory_price = video_cards * video_cards_price* 0.1
total_money = video_cards_price * video_cards + processors_price * processors + ram_memory_price * ram_memory
if video_cards > processors:
    total_money *= 0.85
difference = abs(budget - total_money)
if budget >= total_money:
    print(f"You have {difference:.2f} leva left!")
else:
    print(f"Not enough money! You need {difference:.2f} leva more!")


