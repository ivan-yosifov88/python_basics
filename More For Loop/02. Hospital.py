number_of_days = int(input())
number_of_physician = 7
untreated_patients = 0
treated_patients = 0
sum_treated = 0
sum_untreated = 0
for number_of_days in range(1, number_of_days + 1):
    number_of_patients = int(input())
    if number_of_days % 3 == 0 and sum_untreated > sum_treated:
        number_of_physician += 1
    if number_of_physician < number_of_patients:
        treated_patients = number_of_physician
        untreated_patients = number_of_patients - treated_patients
        sum_untreated += untreated_patients
        sum_treated += treated_patients
    else:
        treated_patients = number_of_patients
        sum_treated += treated_patients
print(f"Treated patients: {sum_treated}.")
print(f"Untreated patients: {sum_untreated}.")




