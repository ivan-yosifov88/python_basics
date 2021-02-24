numbers = int(input())
sum_1 = 0
sum_2 = 0
for numbers in range(0, numbers):
    number1 = int(input())
    sum_1 += number1
for numbers in range(numbers, numbers * 2 + 1):
    number2 = int(input())
    sum_2 += number2
difference = abs(sum_1 - sum_2)
if sum_1 == sum_2:
    print(f"Yes, sum = {sum_1}")
else:
    print(f"No, diff = {difference}")





