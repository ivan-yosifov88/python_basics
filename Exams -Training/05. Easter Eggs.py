import sys
max_eggs = - sys.maxsize
red_counter = 0
orange_counter = 0
blue_counter = 0
green_counter = 0
max_colour = ""
number_of_eggs = int(input())
for eggs in range(number_of_eggs):
    colour_of_egg = input()
    if colour_of_egg == "red":
        red_counter += 1
        if red_counter > max_eggs:
            max_eggs = red_counter
            max_colour = "red"
    elif colour_of_egg == "orange":
        orange_counter += 1
        if orange_counter > max_eggs:
            max_eggs = orange_counter
            max_colour = "orange"
    elif colour_of_egg == "blue":
        blue_counter += 1
        if blue_counter > max_eggs:
            max_eggs = blue_counter
            max_colour = "blue"
    elif colour_of_egg == "green":
        green_counter += 1
        if green_counter > max_eggs:
            max_eggs = green_counter
            max_colour = "green"
print(f"Red eggs: {red_counter}")
print(f"Orange eggs: {orange_counter}")
print(f"Blue eggs: {blue_counter}")
print(f"Green eggs: {green_counter}")
print(f"Max eggs: {max_eggs} -> {max_colour}")
