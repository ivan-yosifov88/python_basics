address_number_n = int(input())
address_number_m = int(input())
special_number_s = int(input())
for numbers in range(address_number_m, address_number_n - 1, - 1):
    if numbers % 2 == 0 and numbers % 3 == 0:
        if numbers == special_number_s:
            break
        else:
            print(numbers, end=" ")