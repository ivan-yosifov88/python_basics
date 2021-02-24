length = int(input())
width = int(input())
height = int(input())
percentage_occupied_volume = float(input())
volume_fish_tank_litres = length * width * height * 0.001
total_litres = volume_fish_tank_litres * (1 - percentage_occupied_volume / 100)
print(total_litres)

