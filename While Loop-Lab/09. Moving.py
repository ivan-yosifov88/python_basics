width = int(input())
length = int(input())
height = int(input())
command = input()
total_space = width * length * height
while command != "Done":
    number_of_boxes = int(command)
    total_space -= number_of_boxes
    if total_space <= 0:
        print(f"No more free space! You need {abs(total_space)} Cubic meters more.")
        break
    command = input()
else:
    print(f"{total_space} Cubic meters left.")
