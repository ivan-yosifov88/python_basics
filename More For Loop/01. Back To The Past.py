inherited_money = float(input())
year_to_the_past = int(input())
years_in_one_century = year_to_the_past - 1800
age = 18
for years_in_one_century in range(years_in_one_century + 1):
    if years_in_one_century % 2 == 0:
        inherited_money -= 12000
    else:
        inherited_money -= 12000 + 50 * age
    age += 1
if inherited_money >= 0:
    print(f"Yes! He will live a carefree life and will have {inherited_money:.2f} dollars left.")
else:
    print(f"He will need {abs(inherited_money):.2f} dollars to survive.")