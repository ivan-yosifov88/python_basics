number_of_judging_jury = int(input())
command = input()
total_grade_sum = 0
presentation_counter = 0
while command != "Finish":
    presentation_name = command
    presentation_counter += 1
    average_grade_sum = 0
    for grades in range(number_of_judging_jury):
        current_grade = float(input())
        average_grade_sum += current_grade
        total_grade_sum += current_grade
    average_grade_for_current_presentation = average_grade_sum / number_of_judging_jury
    print(f"{presentation_name} - {average_grade_for_current_presentation:.2f}.")
    command = input()
total_average_grade = total_grade_sum / presentation_counter / number_of_judging_jury
print(f"Student's final assessment is {total_average_grade:.2f}.")


