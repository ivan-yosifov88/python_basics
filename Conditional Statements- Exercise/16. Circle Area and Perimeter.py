from math import pi, pow
r = float(input())
calculated_area = pow(r , 2) * pi
calculated_perimeter = 2 * pi * r
print(f"{calculated_area:.2f}")
print(f"{calculated_perimeter:.2f}")