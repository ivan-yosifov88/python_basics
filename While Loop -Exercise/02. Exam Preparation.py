number_of_bad_grades = int(input())
ifFails = False
count_bad_grades = 0
grade_sum = 0
number_of_problems = 0
last_problem = ""
name_of_problem = input()
while name_of_problem != "Enough":
    last_problem = name_of_problem
    grade = int(input())
    if grade <= 4:
        count_bad_grades += 1
        number_of_bad_grades -= 1
        if number_of_bad_grades == 0:
            ifFails = True
            break
    grade_sum += grade
    number_of_problems += 1
    name_of_problem = input()
if ifFails:
    print(f"You need a break, {count_bad_grades} poor grades.")
else:
    print(f"Average score: {grade_sum / number_of_problems :.2f}")
    print(f"Number of problems: {number_of_problems}")
    print(f"Last problem: {last_problem}")