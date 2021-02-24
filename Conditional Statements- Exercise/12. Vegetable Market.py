price_vegetables = float(input())
price_fruits = float(input())
weight_vegetables = int(input())
weight_fruits = int(input())
total_sum = price_vegetables * weight_vegetables + price_fruits * weight_fruits
total_sum_in_euro = total_sum / 1.94
print(f"{total_sum_in_euro:.2f}")