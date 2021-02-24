import sys
read_text = input()
max_number = - sys.maxsize
while read_text != "Stop":
    number = int(read_text)
    if number > max_number:
        max_number = number
    read_text = input()
print(max_number)


