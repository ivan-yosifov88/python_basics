first_number = int(input())
second_number = int(input())
first_number_end = int(input())
second_number_end = int(input())
for first_couple in range(first_number, first_number + first_number_end + 1):
    first = first_couple
    for second_couple in range(second_number, second_number + second_number_end + 1):
        second = second_couple
        if (first % first == 0 and first / 1 == first and first % 2 != 0 and first % 3 != 0 and first % 5 != 0 and first % 7 != 0) and (second % second == 0 and second / 1 == second and second % 2 != 0 and second % 3 != 0 and second % 5 != 0 and second % 7 != 0):
            print(f"{first}{second}")
