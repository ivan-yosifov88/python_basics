budget = float(input())
season = input()
money_spend = 0
holiday = ""
destination = ""
if budget <= 100:
    if season == "summer":
        budget *= 0.3
        holiday = "Camp"
    elif season == "winter":
        budget *= 0.7
        holiday = "Hotel"
    destination = "Bulgaria"
elif 100 < budget <= 1000:
    if season == "summer":
        budget *= 0.4
        holiday = "Camp"
    elif season == "winter":
        budget *= 0.8
        holiday = "Hotel"
    destination = "Balkans"
elif budget > 1000:
    budget *= 0.9
    holiday = "Hotel"
    destination = "Europe"
print(f"Somewhere in {destination}")
print(f"{holiday} - {budget:.2f}")




