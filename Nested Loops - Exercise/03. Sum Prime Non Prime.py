command = input()
sum_of_prime_numbers = 0
sum_of_non_prime_numbers = 0
while command != "stop":
    new_number = int(command)
    if new_number < 0:
        print("Number is negative.")
        command = input()
        continue
    is_number_prime = True
    for checking in range(2, new_number):
        if new_number % checking == 0:
            is_number_prime = False
            break
    if is_number_prime:
        sum_of_prime_numbers += new_number
    else:
        sum_of_non_prime_numbers += new_number

    command = input()
print(f"Sum of all prime numbers is: {sum_of_prime_numbers}")
print(f"Sum of all non prime numbers is: {sum_of_non_prime_numbers}")
