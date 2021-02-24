sqare_meters = float(input())
sqare_meters_price = sqare_meters * 7.61
sqare_meters_discount = sqare_meters * 7.61 * 0.18
end_sum = sqare_meters_price - sqare_meters_discount
print(f'The final price is: {end_sum} lv.')
print(f'The discount is: {sqare_meters_discount} lv.')
