numbers_of_chrysanthemums = int(input())
number_of_roses = int(input())
number_of_tulips = int(input())
season = input()
is_day_is_holiday = input()
chrysanthemums_price = 0
roses_price = 0
tulips_price = 0
bouquet_price = 0
if season == "Spring" or season == "Summer":
    chrysanthemums_price = 2
    roses_price = 4.1
    tulips_price = 2.5
elif season == "Autumn" or season == "Winter":
    chrysanthemums_price = 3.75
    roses_price = 4.5
    tulips_price = 4.15
bouquet_price = numbers_of_chrysanthemums * chrysanthemums_price + number_of_roses * roses_price + number_of_tulips * tulips_price
if is_day_is_holiday == "Y":
    bouquet_price *= 1.15
if number_of_tulips > 7 and season == "Spring":
    bouquet_price *= 0.95
if number_of_roses >= 10 and season == "Winter":
    bouquet_price *= 0.9
if (number_of_roses + number_of_tulips + numbers_of_chrysanthemums) > 20:
    bouquet_price *= 0.8
bouquet_price += 2
print(f"{bouquet_price:.2f}")



