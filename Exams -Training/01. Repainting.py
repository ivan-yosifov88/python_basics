needed_nylon = int(input())
needed_paint = int(input())
paint_thinner = int(input())
hours_of_work = int(input())
needed_paint *= 1.1
needed_nylon += 2
materials_cost = 0.40 + needed_nylon * 1.5 + needed_paint * 14.5 + paint_thinner * 5
workers_money_for_hour = materials_cost * 0.3
total_money = workers_money_for_hour * hours_of_work + materials_cost
print(f"Total expenses: {total_money:.2f} lv.")