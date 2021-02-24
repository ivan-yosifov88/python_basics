in_number = float(input())
in_unit = input()
converted_unit = input()
if in_unit == "m":
    if converted_unit == "cm":
        result = in_number * 100
    elif converted_unit == "mm":
        result = in_number * 1000
elif in_unit == "cm":
    if converted_unit == "m":
        result = in_number / 100
    elif converted_unit == "mm":
        result = in_number * 10
elif in_unit == "mm":
    if converted_unit == "cm":
        result = in_number / 10
    elif converted_unit == "m":
        result = in_number / 1000
print(f"{result:.3f}")
