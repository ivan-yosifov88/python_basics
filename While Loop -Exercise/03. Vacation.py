needed_money = float(input())
money_on_hand = float(input())
days_spend = 0
total_days = 0
money_collected = False
while needed_money > money_on_hand:
    command = input()
    money = float(input())
    total_days += 1
    if command == "spend":
        money_collected = False
        days_spend += 1
        money_on_hand -= money
        if money_on_hand < 0:
            money_on_hand = 0
        if days_spend == 5:
            break

    elif command == "save":
        money_on_hand += money
        days_spend = 0
        money_collected = True

if money_collected:
    print(f"You saved the money for {total_days} days.")
else:
    print("You can't save the money.")
    print(f"{total_days}")
