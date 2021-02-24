command = input()
max_sum = 0
word_max = ""
while command != "End of words":
    new_word = command
    sum_of_digits = 0
    for index, digit in enumerate(new_word):
        sum_of_digits += ord(digit)
    if ord(new_word[0]) == 65 or ord(new_word[0]) == 69 or ord(new_word[0]) == 73 or ord(new_word[0]) == 79 or ord(new_word[0]) == 85 or ord(new_word[0]) == 89 or ord(new_word[0]) == 97 or ord(new_word[0]) == 101 or ord(new_word[0]) == 105 or ord(new_word[0]) == 111 or ord(new_word[0]) == 117 or ord(new_word[0]) == 121:
        sum_of_digits *= len(new_word)
    else:
        sum_of_digits = int(sum_of_digits / len(new_word))
    if max_sum < sum_of_digits:
        max_sum = sum_of_digits
        word_max = new_word
    command = input()
print(f"The most powerful word is {word_max} - {max_sum}")