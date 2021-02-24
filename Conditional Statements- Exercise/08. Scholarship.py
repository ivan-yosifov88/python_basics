income = float(input())
average_success = float(input())
minimal_salary = float(input())
social_scholarship = int(minimal_salary * 0.35)
excellent_scholarship = int(average_success * 25)
if average_success >= 5.5:
    if income < minimal_salary:
        if excellent_scholarship >= social_scholarship:
            print(f"You get a scholarship for excellent results {excellent_scholarship} BGN")
        else:
            print(f"You get a Social scholarship {social_scholarship} BGN")
    else:
        print(f"You get a scholarship for excellent results {excellent_scholarship} BGN")

elif 4.5 < average_success < 5.5:
    if income < minimal_salary:
        print(f"You get a Social scholarship {social_scholarship} BGN")
    else:
        print("You cannot get a scholarship!")
else:
    print("You cannot get a scholarship!")