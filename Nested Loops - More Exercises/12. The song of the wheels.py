control_number = int(input())
correct_password_counter = 0
is_four_pass = False
for first_number in range(1, 10):
    for second_number in range(1, 10):
        for third_number in range(1, 10):
            for fourth_number in range(1, 10):
                if first_number < second_number and third_number > fourth_number:
                    if control_number == first_number * second_number + third_number * fourth_number:
                        correct_password_counter += 1
                        print(f"{first_number}{second_number}{third_number}{fourth_number}", end=" ")
                        if correct_password_counter == 4:
                            current_first = first_number
                            current_second = second_number
                            current_third = third_number
                            current_fourth = fourth_number
                            is_four_pass = True
print()
if is_four_pass:
    print(f"Password: {current_first}{current_second}{current_third}{current_fourth}")
if correct_password_counter < 5:
    print("No!")

