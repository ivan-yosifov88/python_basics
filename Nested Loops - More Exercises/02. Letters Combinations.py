start_letter = input()
end_letter = input()
special_letter = input()
number_of_valid_combinations = 0
for first_number in range (ord(start_letter), ord(end_letter) + 1):
    for second_number in range(ord(start_letter), ord(end_letter) + 1):
        for third_number in range(ord(start_letter), ord(end_letter) + 1):
            if first_number == ord(special_letter) or second_number == ord(special_letter) or third_number == ord(special_letter):
                continue
            else:
                number_of_valid_combinations += 1
                print(f"{chr(first_number)}{chr(second_number)}{chr(third_number)}", end =" " )
print(number_of_valid_combinations)




