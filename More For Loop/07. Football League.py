stadium_capacity = int(input())
number_of_all_fans = int(input())
number_in_a = 0
number_in_b = 0
number_in_v = 0
number_in_g = 0
for number_of_all_fans in range(1, number_of_all_fans + 1):
    sector_type = input()
    if sector_type == "A":
        number_in_a += 1
    if sector_type == "B":
        number_in_b += 1
    if sector_type == "V":
        number_in_v += 1
    if sector_type == "G":
        sector_type = 1
        number_in_g += 1
fans_in_a_percent = number_in_a / number_of_all_fans * 100
fans_in_b_percent = number_in_b / number_of_all_fans * 100
fans_in_v_percent = number_in_v / number_of_all_fans * 100
fans_in_g_percent = number_in_g / number_of_all_fans * 100
percent_fans_relative_to_stadium = (number_in_a + number_in_b + number_in_v + number_in_g) / stadium_capacity * 100
print(f"{fans_in_a_percent:.2f}%")
print(f"{fans_in_b_percent:.2f}%")
print(f"{fans_in_v_percent:.2f}%")
print(f"{fans_in_g_percent:.2f}%")
print(f"{percent_fans_relative_to_stadium:.2f}%")