hight_of_house = float(input())
lenght_of_side_wall = float(input())
hight_of_the_roof = float(input())
front_and_back_walls = hight_of_house * hight_of_house * 2 - 1.2 * 2
side_walls = hight_of_house * lenght_of_side_wall * 2 - 1.5 * 1.5 * 2
all_walls = front_and_back_walls + side_walls
roof_front_and_back = hight_of_house * hight_of_the_roof * 2 / 2
roof_sides = hight_of_house * lenght_of_side_wall * 2
roof_area = roof_front_and_back + roof_sides
needed_paint_sides = all_walls / 3.4
needed_pain_roof = roof_area / 4.3
print(f"{needed_paint_sides:.2f}")
print(f"{needed_pain_roof:.2f}")
