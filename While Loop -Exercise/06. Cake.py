width = int(input())
length = int(input())
cake_size = width * length
command = input()
no_more_cake = False
while command != "STOP":
    number_of_pieces = int(command)
    cake_size -= number_of_pieces
    if cake_size < 0:
        break
    command = input()
if cake_size >= 0:
    print(f"{cake_size} pieces are left." )
else:
    print(f"No more cake left! You need {abs(cake_size)} pieces more.")