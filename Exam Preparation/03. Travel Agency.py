
# ена за ден	Банско/Боровец	Варна/Бургас
# 	с екипировка	без екипировка	със закуска	без закуска
# 	100лв.	80лв	130лв.	100лв.
# VIP отстъпка	10%	5%	12%	7%
# Ако клиентът е заявил престой повече от 7 дни, получава единия ден безплатно.
# Вход
# От конзолата се четат 4 реда:
# 1.	Име на града - текст с възможности ("Bansko",  "Borovets", "Varna" или "Burgas")
# 2.	Вид на пакета - текст с възможности ("noEquipment",  "withEquipment", "noBreakfast" или "withBreakfast")
# 3.	Притежание на VIP отстъпка - текст с възможности  "yes" или "no"
# 4.	Дни за престой - цяло число в интервала [1 … 10000]
# Изход
# На конзолата се отпечатва 1 ред:
# •	Когато потребителят е въвел всички данни правилно, отпечатваме:
# "The price is {цената, форматирана до втория знак}lv! Have a nice time!"

name_of_town = input()
name_of_package = input()
possessing_vip_card = input()
days_stay = int(input())
price_per_day = 0
discount = 0
total_price = 0
is_valid_input = True
if days_stay < 1:
    print("Days must be positive number!")
else:
    if name_of_town == "Bansko" or name_of_town == "Borovets" and is_valid_input :
        if name_of_package == "withEquipment":
            price_per_day = 100
            discount = 0.1
        elif name_of_package == "noEquipment":
            price_per_day = 80
            discount = 0.05
        else:
            is_valid_input = False
            print("Invalid input!")
    elif name_of_town == "Varna" or name_of_town == "Burgas" and is_valid_input:
        if name_of_package == "withBreakfast":
            price_per_day = 130
            discount = 0.12
        elif name_of_package == "noBreakfast":
            price_per_day = 100
            discount = 7
        else:
            is_valid_input = False
            print("Invalid input!")
    else:
        is_valid_input = False
        print("Invalid input!")
    if is_valid_input:
        if possessing_vip_card == "yes":
            price_per_day -= price_per_day * discount
        total_price = price_per_day * days_stay
        if days_stay > 7:
            total_price = price_per_day * (days_stay -1)
        print(f"The price is {total_price:.2f}lv! Have a nice time!")
