for numbers in range(1, 100):
    number = float(input())
    if number >= 0:
        number *= 2
        print(f"Result: {number:.2f}")
    else:
        print("Negative number!")
        break