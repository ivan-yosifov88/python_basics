number_of_students = int(input())
fail_evaluation = 0
middle_evaluation = 0
good_evaluation = 0
excellent_evaluation = 0
fail_numbers = 0
middle_numbers = 0
good_number = 0
excellent_number = 0
for number_of_students in range(1, number_of_students + 1):
    exam_evaluation = float(input())
    if exam_evaluation < 3:
        fail_numbers += 1
        fail_evaluation += exam_evaluation
    elif 3 <= exam_evaluation <= 3.99:
        middle_numbers += 1
        middle_evaluation += exam_evaluation
    elif 4 <= exam_evaluation <= 4.99:
        good_number += 1
        good_evaluation += exam_evaluation
    elif exam_evaluation >= 5:
        excellent_number += 1
        excellent_evaluation += exam_evaluation
average_evaluation = (fail_evaluation + middle_evaluation + good_evaluation + excellent_evaluation) / number_of_students
top_students = excellent_number / number_of_students * 100
between_four_and_five = good_number/ number_of_students * 100
between_three_and_four = middle_numbers/ number_of_students * 100
fail_students = fail_numbers / number_of_students * 100
print(f"Top students: {top_students:.2f}%")
print(f"Between 4.00 and 4.99: {between_four_and_five:.2f}%")
print(f"Between 3.00 and 3.99: {between_three_and_four:.2f}%")
print(f"Fail: {fail_students:.2f}%")
print(f"Average: {average_evaluation:.2f}")

