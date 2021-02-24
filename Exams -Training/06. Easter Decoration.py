number_of_clients = int(input())
total_sum = 0
for clients in range(number_of_clients):
    command = input()
    basket_price = 1.5
    wreath_price = 3.8
    chocolate_binny_price = 7
    current_sum = 0
    counter_product = 0
    while command != "Finish":
        product = command
        counter_product += 1
        if product == "basket":
            current_sum += basket_price
        elif product == "wreath":
            current_sum += wreath_price
        elif product == "chocolate bunny":
            current_sum += chocolate_binny_price
        command = input()
    if counter_product % 2 == 0:
        current_sum *= 0.8
    print(f"You purchased {counter_product} items for {current_sum:.2f} leva.")
    total_sum += current_sum
total_sum /= number_of_clients
print(f"Average bill per client is: {total_sum:.2f} leva.")
