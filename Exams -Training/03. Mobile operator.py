term_of_contract = input()
type_of_contract = input()
mobile_internet = input()
number_of_months = int(input())
price_for_month = 0
if term_of_contract == "one":
    if type_of_contract == "Small":
        price_for_month = 9.98
    elif type_of_contract == "Middle":
        price_for_month = 18.99
    elif type_of_contract == "Large":
        price_for_month = 25.98
    elif type_of_contract == "ExtraLarge":
        price_for_month = 35.99
elif term_of_contract == "two":
    if type_of_contract == "Small":
        price_for_month = 8.58
    elif type_of_contract == "Middle":
        price_for_month = 17.09
    elif type_of_contract == "Large":
        price_for_month = 23.59
    elif type_of_contract == "ExtraLarge":
        price_for_month = 31.79
if mobile_internet == "yes":
    if price_for_month <= 10:
        price_for_month += 5.5
    elif 10 < price_for_month <= 30:
        price_for_month += 4.35
    elif price_for_month > 30:
        price_for_month += 3.85

if term_of_contract == "two":
    price_for_month *= 0.9625
total_price = number_of_months * price_for_month
print(f"{total_price:.2f} lv.")

