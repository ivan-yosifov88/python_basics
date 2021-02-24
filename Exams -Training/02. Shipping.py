budget = float(input())
number_video_carts = int(input())
number_processors = int(input())
number_rams = int(input())
price_of_processor = 0.35 * 250 * number_video_carts
price_of_ram = 0.1 * 250 * number_video_carts
end_sum = number_video_carts * 250 + number_processors * price_of_processor + number_rams * price_of_ram
if number_video_carts > number_processors:
    end_sum *= 0.85
difference = abs(budget - end_sum)
if budget >= end_sum:
    print(f"You have {difference:.2f} leva left!")
else:
    print(f"Not enough money! You need {difference:.2f} leva more!")
