footsteps_target = 10000
total_footsteps = 0
command = input()
footstepsReached = False
while command != "Going home":
    number_of_steps = int(command)
    total_footsteps += number_of_steps
    if total_footsteps >= footsteps_target:
        footstepsReached = True
        break
    command = input()
if command == "Going home":
    last_steps = int(input())
    total_footsteps += last_steps
    if total_footsteps >= footsteps_target:
        footstepsReached = True
difference = abs(total_footsteps - footsteps_target)
if footstepsReached:
    print("Goal reached! Good job!")
    print(f"{difference} steps over the goal!")
else:
    print(f"{difference} more steps to reach goal.")