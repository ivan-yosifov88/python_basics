
command = input()
counter_letter_c = 0
counter_letter_o = 0
counter_letter_n = 0
new_word = ""
while command != "End":
    letter = command
    if 65 <= ord(command) <= 90 or 97 <= ord(command) <= 122:
        if command == "c":
            counter_letter_c += 1
            if counter_letter_c == 1:
                command = ""
        elif command == "o":
            counter_letter_o += 1
            if counter_letter_o == 1:
                command = ""
        elif command == "n":
            counter_letter_n += 1
            if counter_letter_n == 1:
                command = ""

        if counter_letter_c >= 1 and counter_letter_o >= 1 and counter_letter_n >= 1:
            print(new_word, end= " ")
            counter_letter_c = 0
            counter_letter_o = 0
            counter_letter_n = 0
            new_word = ""
        new_word += command
    command = input()