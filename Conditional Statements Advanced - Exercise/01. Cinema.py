type_of_screening = input()
rows = int(input())
columns = int(input())
price = 0
if type_of_screening == "Premiere":
    price = 12
elif type_of_screening == "Normal":
    price = 7.5
elif type_of_screening == "Discount":
    price = 5
total_sum = price * rows * columns
print(f"{total_sum:.2f} leva")




