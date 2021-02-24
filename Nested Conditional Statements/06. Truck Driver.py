season = input()
kilometers_for_month = float(input())
earned_money = 0
if kilometers_for_month <= 5000:
    if season == "Spring" or season == "Autumn":
        price = kilometers_for_month * 4 * 0.75
    elif season == "Summer":
        price = kilometers_for_month * 4 * 0.90
    elif season == "Winter":
        price = kilometers_for_month * 4 * 1.05
elif 5000 < kilometers_for_month <= 10000:
    if season == "Spring" or season == "Autumn":
        price = kilometers_for_month * 4 * 0.95
    elif season == "Summer":
        price = kilometers_for_month * 4 * 1.1
    elif season == "Winter":
        price = kilometers_for_month * 4 * 1.25
elif 10000 < kilometers_for_month <= 20000:
    if season == "Spring" or season == "Summer" or season == "Autumn" or season == "Winter":
        price = kilometers_for_month * 4 * 1.45
price *= 0.9
print(f"{price:.2f}")