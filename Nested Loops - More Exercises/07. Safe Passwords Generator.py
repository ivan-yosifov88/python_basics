number_a = int(input())
number_b = int(input())
max_passwords = int(input())
is_pass_over = False
first_letter = 34
second_letter = 63
for first_number in range(1 , number_a + 1):
    for second_number in range(1 , number_b + 1):
        first_letter += 1
        if first_letter > 55:
            first_letter = 35
        second_letter += 1
        if second_letter > 96:
            second_letter = 64
        max_passwords -= 1
        if max_passwords < 0:
            is_pass_over = True
            break
        print(f"{chr(first_letter)}{chr(second_letter)}{first_number}{second_number}{chr(second_letter)}{chr(first_letter)}|", end="")
    if is_pass_over:
        break