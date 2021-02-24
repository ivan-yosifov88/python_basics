numbers = int(input())
sum_even = 0
sum_odd = 0
for numbers in range(1, numbers + 1):
    number = int(input())
    if numbers % 2 == 0:
        sum_even += number
    else:
        sum_odd += number
difference = abs(sum_odd - sum_even)
if sum_odd == sum_even:
    print("Yes")
    print(f"Sum = {sum_odd}")
else:
    print("No")
    print(f"Diff = {difference}")

