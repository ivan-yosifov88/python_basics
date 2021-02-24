voucher_price = int(input())
command = input()
number_of_tickets = 0
number_of_other_products = 0
products_price = 0
while command != "End":
    purchase = command
    if len(purchase) > 8:
        products_price += ord(purchase[0]) + ord(purchase[1])
        if voucher_price >= products_price:
            number_of_tickets += 1
            voucher_price -= products_price
            if voucher_price == products_price:
                break
        else:
            break
    else:
        products_price += ord(purchase[0])
        if voucher_price >= products_price:
            number_of_other_products += 1
            voucher_price -= products_price
            if voucher_price == products_price:
                break
        else:
            break
    products_price = 0
    command = input()
print(f"{number_of_tickets}")
print(f"{number_of_other_products}")