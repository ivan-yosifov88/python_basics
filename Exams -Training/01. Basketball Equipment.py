fee_for_one_year = int(input())
sneakers = fee_for_one_year * 0.60
outfit = sneakers * 0.8
ball = outfit / 4
accessories = ball / 5
total_sum = sneakers + outfit + ball + accessories + fee_for_one_year
print(f"{total_sum:.2f}")