first_result = input()
second_result = input()
third_result = input()
wins = 0
lost = 0
drawn = 0
if ord(first_result[0]) > ord(first_result[2]):
    wins += 1
elif ord(first_result[0]) < ord(first_result[2]):
    lost += 1
elif ord(first_result[0]) == ord(first_result[2]):
    drawn += 1
if ord(second_result[0]) > ord(second_result[2]):
    wins += 1
elif ord(second_result[0]) < ord(second_result[2]):
    lost += 1
elif ord(second_result[0]) == ord(second_result[2]):
    drawn += 1
if ord(third_result[0]) > ord(third_result[2]):
    wins += 1
elif ord(third_result[0]) < ord(third_result[2]):
    lost += 1
elif ord(third_result[0]) == ord(third_result[2]):
    drawn += 1
print(f"Team won {wins} games.")
print(f"Team lost {lost} games.")
print(f" Drawn games: {drawn}")


