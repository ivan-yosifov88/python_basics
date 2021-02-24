needed_hours = int(input())
days_for_project = int(input())
number_of_employees = int(input())
days_with_training = days_for_project * 0.9
work_hours = int(days_with_training * 8 + number_of_employees * 2 * days_for_project)
difference = abs(needed_hours - work_hours)
if needed_hours <= work_hours:
    print(f"Yes!{difference} hours left.")
else:
    print(f"Not enough time!{difference} hours needed.")