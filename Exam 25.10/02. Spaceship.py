width = float(input())
length = float(input())
height = float(input())
astronaut_height = float(input())
needed_space_for_one_astronaut = 2 * 2 * (astronaut_height + 0.4)
spaceship_dimensions = width * length * height
number_of_astronaut = spaceship_dimensions // needed_space_for_one_astronaut
if 3 <= number_of_astronaut <= 10:
    print(f"The spacecraft holds {int(number_of_astronaut)} astronauts.")
elif number_of_astronaut < 3:
    print("The spacecraft is too small.")
elif number_of_astronaut > 10:
    print("The spacecraft is too big.")