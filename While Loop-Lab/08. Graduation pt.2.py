name_of_student = input()
fails = 0
average_grade_sum = 0
studentEjected = False
current_class = 1
while True:
    student_grade = float(input())
    if student_grade < 4:
        fails += 1
        if fails == 2:
            studentEjected = True
            break
    else:
        average_grade_sum += student_grade
        if current_class == 12:
                break
        current_class += 1
if studentEjected:
    print(f"{name_of_student} has been excluded at {current_class} grade")
else:
    print(f"{name_of_student} graduated. Average grade: {average_grade_sum / current_class:.2f}")