number_days = int(input())
number_hours = int(input())
price_for_parking = 0
total_sum = 0
for days in range(1, number_days + 1):
    current_sum = 0
    for hours in range(1, number_hours + 1):
        if days % 2 == 0 and hours % 2 == 1:
            price_for_parking = 2.5
        elif days % 2 == 1 and hours % 2 == 0:
            price_for_parking = 1.25
        else:
            price_for_parking = 1
        current_sum += price_for_parking
    print(f"Day: {days} - {current_sum:.2f} leva")
    total_sum += current_sum
print(f"Total: {total_sum:.2f} leva")
