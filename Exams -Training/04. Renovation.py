from math import ceil
height = int(input())
width = int(input())
percent_not_paint_area = int(input())
wall_area = height * width * 4
not_paint_area = wall_area * percent_not_paint_area / 100
room_area = ceil(wall_area - not_paint_area)
painted_area = 0
command = input()
is_all_walls_painted = False
is_paint_left = False
while command != "Tired!":
    litres_paint = int(command)
    painted_area += litres_paint
    if painted_area == room_area:
        is_all_walls_painted = True
        break
    elif painted_area > room_area:
        is_paint_left = True
        break
    command = input()
difference = abs(room_area - painted_area)
if is_all_walls_painted:
    print("All walls are painted! Great job, Pesho!" )
elif is_paint_left:
    print(f"All walls are painted and you have {difference} l paint left!")
else:
    print(f"{difference} quadratic m left.")