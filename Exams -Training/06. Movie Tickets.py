number_a1 = int(input())
number_a2 = int(input())
n = int(input())
end_third_symbol = int(n / 2)
for first_symbol in range(number_a1, number_a2):
    for second_symbol in range(1, n):
        for third_symbol in range(1, end_third_symbol):
            if first_symbol % 2 != 0 and (second_symbol + third_symbol + first_symbol) % 2 != 0:
                print(f"{chr(first_symbol)}-{second_symbol}{third_symbol}{first_symbol}")