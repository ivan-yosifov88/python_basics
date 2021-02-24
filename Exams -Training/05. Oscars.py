actor_name = input()
start_points = float(input())
needed_points = 1250.5
is_point_enough = False
number_of_evaluators = int(input())
total_points = start_points
for evaluators in range(number_of_evaluators):
    name_of_judge = input()
    point_of_judge = float(input())
    current_points = len(name_of_judge) * point_of_judge / 2
    total_points += current_points
    if needed_points <= total_points:
        is_point_enough = True
        break
if is_point_enough:
    print(f"Congratulations, {actor_name} got a nominee for leading role with {total_points:.1f}!")
else:
    difference = abs(needed_points - total_points)
    print(f"Sorry, {actor_name} you need {difference:.1f} more!")
