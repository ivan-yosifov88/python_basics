number_days_campaign = int(input())
number_cake_bakers = int(input())
number_of_cakes = int(input())
number_of_waffles = int(input())
number_of_pancakes = int(input())
cake_profit = number_of_cakes * 45
waffles_profit = number_of_waffles * 5.8
pancakes_profit = number_of_pancakes * 3.2
collected_money = number_days_campaign * number_cake_bakers * (cake_profit + waffles_profit + pancakes_profit)
campaign_cost = collected_money / 8
total_collected_money = collected_money - campaign_cost
print(total_collected_money)