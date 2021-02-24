needed_nylon = int(input())
needed_paint = int(input())
quantity_thinner = int(input())
work_hours = int(input())
total_sum = (needed_nylon + 2)* 1.5 + needed_paint * 14.5 * 1.1 + quantity_thinner * 5 + 0.4
workers_payment = total_sum * 0.3 * work_hours
total_sum += workers_payment
print(f"Total expenses: {total_sum:.2f} lv.")