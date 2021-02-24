w = float(input())
h = float(input())
h_without_corridor = h - 1
length = w // 1.2
weight = h_without_corridor // 0.7
total_work_places = length * weight - 3
print(total_work_places)

