city = input()
sales = float(input())
commission = 0
is_city_valid = True
is_sales_valid = True
if 0 <= sales <= 500:
    if city == "Sofia":
        commission = 0.05
    elif city == "Varna":
        commission = 0.045
    elif city == "Plovdiv":
        commission = 0.055
    else:
        is_city_valid = False
elif 500 < sales <= 1000:
    if city == "Sofia":
        commission = 0.07
    elif city == "Varna":
        commission = 0.075
    elif city == "Plovdiv":
        commission = 0.08
    else:
        is_city_valid = False
elif 1000 < sales <= 10000:
    if city == "Sofia":
        commission = 0.08
    elif city == "Varna":
        commission = 0.10
    elif city == "Plovdiv":
        commission = 0.12
    else:
        is_city_valid = False
elif sales > 10000:
    if city == "Sofia":
        commission = 0.12
    elif city == "Varna":
        commission = 0.13
    elif city == "Plovdiv":
        commission = 0.145
    else:
        is_city_valid = False
else:
    is_sales_valid = False
if is_city_valid and is_sales_valid:
    print(f"{(sales * commission):.2f}")
else:
    print("error")




