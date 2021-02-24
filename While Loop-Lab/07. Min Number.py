import sys
read_text = input()
min_number = sys.maxsize
while read_text != "Stop":
    number = int(read_text)
    if number < min_number:
        min_number = number
    read_text = input()
print(min_number)


