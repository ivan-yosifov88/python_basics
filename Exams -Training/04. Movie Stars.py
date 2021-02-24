budget = float(input())
command = input()
is_budget_over = False
while not command == "ACTION":
    actor_name = command
    if len(actor_name) > 15:
        actor_salary = 0.2 * budget
    else:
        actor_salary = float(input())
    budget -= actor_salary
    if budget <= 0:
        is_budget_over = True
        break
    command = input()
if is_budget_over:
    print(f"We need {abs(budget):.2f} leva for our actors.")
else:
    print(f"We are left with {budget:.2f} leva.")