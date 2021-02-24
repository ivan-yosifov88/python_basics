
price_of_flour = float(input())
weight_of_flour = float(input())
weight_of_sugar = float(input())
number_eggshells = int(input())
number_yeast = int(input())
price_of_sugar = price_of_flour * 0.75
price_of_eggshells = price_of_flour * 1.1
price_of_yeast = price_of_sugar * 0.2
total_sum = price_of_flour * weight_of_flour + price_of_sugar * weight_of_sugar + price_of_eggshells * number_eggshells + price_of_yeast * number_yeast
print(f"{total_sum:.2f}")
