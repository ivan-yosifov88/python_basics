fruit = input()
day = input()
quantity = float(input())
price = 0
is_fruit_valid = True
is_day_valid = True
if day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday" or day == "Friday":
    if fruit == "banana":
        price = 2.5 * quantity
    elif fruit == "apple":
        price = 1.2 * quantity
    elif fruit == "orange":
        price = 0.85 * quantity
    elif fruit == "grapefruit":
        price = 1.45 * quantity
    elif fruit == "kiwi":
        price = 2.7 * quantity
    elif fruit == "pineapple":
        price = 5.5 * quantity
    elif fruit == "grapes":
        price = 3.85 * quantity
    else:
        is_fruit_valid = False
elif day == "Saturday" or day == "Sunday":
    if fruit == "banana":
        price = 2.7 * quantity
    elif fruit == "apple":
        price = 1.25 * quantity
    elif fruit == "orange":
        price = 0.9 * quantity
    elif fruit == "grapefruit":
        price = 1.6 * quantity
    elif fruit == "kiwi":
        price = 3 * quantity
    elif fruit == "pineapple":
        price = 5.6 * quantity
    elif fruit == "grapes":
        price = 4.2 * quantity
    else:
        is_fruit_valid = False
else:
    is_day_valid = False
if is_fruit_valid and is_day_valid:
    print(f"{price:.2f}")
else:
    print("error")
