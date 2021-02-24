expected_amount = int(input())
command = input()
product_counter = 0
cash_payment = 0
cart_payment = 0
valid_cash_payment = 0
valid_card_payment = 0
money_is_collected = False
while not command == "End":
    product = int(command)
    product_counter += 1
    if product_counter == 1:
        if product > 100:
            print("Error in transaction!")
        else:
            print("Product sold!")
            cash_payment += product
            valid_cash_payment += 1
    if product_counter == 2:
        if product < 10:
            print("Error in transaction!")
        else:
            print("Product sold!")
            cart_payment += product
            valid_card_payment += 1
        product_counter = 0
    total_valid_payment = cash_payment + cart_payment
    if expected_amount <= total_valid_payment:
        money_is_collected = True
        break
    command = input()
if money_is_collected:
    print(f"Average CS: {(cash_payment / valid_cash_payment):.2f}")
    print(f"Average CC: {(cart_payment / valid_card_payment):.2f}")
else:
    print("Failed to collect required money for charity.")
