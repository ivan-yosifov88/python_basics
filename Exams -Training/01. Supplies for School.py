number_packs_of_pens = int(input())
number_packs_of_markers = int(input())
litre_of_cleaning_detergent = float(input())
percent_discount = int(input())
total_sum = number_packs_of_pens * 5.8 + number_packs_of_markers * 7.2 + litre_of_cleaning_detergent * 1.2
total_sum_with_discount = total_sum * (100 - percent_discount) / 100
print(f"{total_sum_with_discount:.3f}")