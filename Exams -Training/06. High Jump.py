end_jump = int(input())
start_jump = end_jump - 30
number_of_tries = 0
is_failed = False
for jump_to_beat in range(start_jump, end_jump + 1, 5):
    jump = int(input())
    number_of_tries += 1
    if jump <= jump_to_beat:
        for new_try in range (2):
            number_of_tries += 1
            new_jump = int(input())
            if new_jump <= jump_to_beat:
                if new_try == 1:
                    is_failed = True
                    break
            else:
                break
    if is_failed:
        break
if is_failed:
    print(f"Tihomir failed at {jump_to_beat}cm after {number_of_tries} jumps.")
else:
    print(f"Tihomir succeeded, he jumped over {jump_to_beat}cm after {number_of_tries} jumps.")