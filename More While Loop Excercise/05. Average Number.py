number = int(input())
sum_numbers = 0
for numbers in range(number):
    new_number = int(input())
    sum_numbers += new_number
sum_numbers /= number
print(f"{sum_numbers:.2f}")
