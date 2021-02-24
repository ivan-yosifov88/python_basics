hall_capacity = int(input())
is_hall_full = False
command = input()
total_visitors = 0
total_price = 0
while not command == "Movie time!":
    new_visitors = int(command)
    if hall_capacity >= new_visitors:
        total_visitors += new_visitors
        hall_capacity -= new_visitors
        total_price += new_visitors * 5
        if (new_visitors * 5) % 3 == 0:
            total_price -= 5
    elif hall_capacity < new_visitors:
        is_hall_full = True
        break
    command = input()
if is_hall_full:
    print("The cinema is full.")
else:
    print(f"There are {hall_capacity} seats left in the cinema.")
print(f"Cinema income - {total_price} lv.")