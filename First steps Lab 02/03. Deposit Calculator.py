deposit_sum = float(input())
deposit_term = int(input())
annual_interest_rate = float(input())
final_sum = deposit_sum + deposit_term * deposit_sum * annual_interest_rate / 100 /12
print(final_sum)

