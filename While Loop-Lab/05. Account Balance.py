money = input()
total_sum = 0
while money != "NoMoreMoney":
    installment = float(money)
    if installment < 0:
        print("Invalid operation!")
        break
    total_sum += installment
    print(f"Increase: {installment:.2f}")
    money = input()
print(f"Total: {total_sum:.2f}")
