number_of_chicken_menus = int(input())
number_of_fish_menus = int(input())
number_of_vegetarian_menus = int(input())
price_of_order = number_of_chicken_menus * 10.35 + number_of_fish_menus * 12.4 + number_of_vegetarian_menus * 8.15
total_sum = price_of_order * 1.2 + 2.50
print(f"Total: {total_sum:.2f}")
