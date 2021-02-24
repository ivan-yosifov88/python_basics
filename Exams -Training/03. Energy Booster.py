type_of_fruit = input()
set_size = input()
number_of_orders = int(input())
price = 0
order = 0
if set_size == "small":
    if type_of_fruit == "Watermelon":
        price = 56 * 2
    elif type_of_fruit == "Mango":
        price = 36.66 * 2
    elif type_of_fruit == "Pineapple":
        price = 42.1 * 2
    elif type_of_fruit == "Raspberry":
        price = 20 * 2
elif set_size == "big":
    if type_of_fruit == "Watermelon":
        price = 28.7 * 5
    elif type_of_fruit == "Mango":
        price = 19.6 * 5
    elif type_of_fruit == "Pineapple":
        price = 24.8 * 5
    elif type_of_fruit == "Raspberry":
        price = 15.2 * 5
order = number_of_orders * price
if 400 <= order <= 1000:
    order *= 0.85
elif order > 1000:
    order *= 0.5
print(f"{order:.2f} lv.")