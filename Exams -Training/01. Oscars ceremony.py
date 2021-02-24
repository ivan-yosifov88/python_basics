rent_of_hall = int(input())
statuettes_price = rent_of_hall * 0.7
catering_price = statuettes_price * 0.85
sound_system_price = catering_price / 2
total_money = rent_of_hall + statuettes_price + catering_price + sound_system_price
print(f"{total_money:.2f}")
