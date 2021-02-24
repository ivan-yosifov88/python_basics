period_in_months = int(input())
electricity_costs = 0
other_costs = 0
for period_in_months in range(1, period_in_months + 1):
    electricity_bill = float(input())
    electricity_costs += electricity_bill
    other_bill = (electricity_bill + 20 + 15) * 1.2
    other_costs += other_bill
water_costs = period_in_months * 20
internet_costs = period_in_months * 15
averige_costs = (electricity_costs + other_costs + water_costs + internet_costs) / period_in_months
print(f"Electricity: {electricity_costs:.2f} lv")
print(f"Water: {water_costs:.2f} lv")
print(f"Internet: {internet_costs:.2f} lv")
print(f"Other: {other_costs:.2f} lv")
print(f"Average: {averige_costs:.2f} lv")


