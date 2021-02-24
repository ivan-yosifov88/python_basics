number = int(input())
p1 = 0
p2 = 0
p3 = 0
for numbers in range(number):
    new_number = int(input())
    if new_number % 2 == 0:
        p1 += 1
    if new_number % 3 == 0:
        p2 += 1
    if new_number % 4 == 0:
        p3 += 1
p1_percent = p1 / number * 100
p2_percent = p2 / number * 100
p3_percent = p3 / number * 100
print(f"{p1_percent:.2f}%")
print(f"{p2_percent:.2f}%")
print(f"{p3_percent:.2f}%")
