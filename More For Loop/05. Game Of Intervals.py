number_of_moves = int(input())
score = 0
first_row = 0
second_row = 0
third_row = 0
fourth_row = 0
fifth_row = 0
sixth_row = 0
for number_of_moves in range(1, number_of_moves + 1):
    move = int(input())
    if 0 <= move <= 9:
        first_row += 1
        score += 0.2 * move
    elif 10 <= move <= 19:
        second_row += 1
        score += 0.3 * move
    elif 20 <= move <= 29:
        third_row += 1
        score += 0.4 * move
    elif 30 <= move <= 39:
        fourth_row += 1
        score += 50
    elif 40 <= move <= 50:
        fifth_row += 1
        score += 100
    elif move < 0 or move > 50:
        sixth_row += 1
        score /= 2
print(f"{score:.2f}")
print(f"From 0 to 9: {(first_row / number_of_moves * 100):.2f}%")
print(f"From 10 to 19: {(second_row / number_of_moves * 100):.2f}%")
print(f"From 20 to 29: {(third_row / number_of_moves * 100):.2f}%")
print(f"From 30 to 39: {(fourth_row / number_of_moves * 100):.2f}%")
print(f"From 40 to 50: {(fifth_row/ number_of_moves * 100):.2f}%")
print(f"Invalid numbers: {(sixth_row / number_of_moves * 100):.2f}%")


