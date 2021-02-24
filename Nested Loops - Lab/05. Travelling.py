command = input()
while command != "End":
    budget = float(input())
    total_save_money = 0
    while total_save_money < budget:
        save_money = float(input())
        total_save_money += save_money
    else:
        print(f"Going to {command}!")
    command = input()




