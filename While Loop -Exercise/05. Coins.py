change = float(input())
coins_counter = 0
coins = int(change * 100)

coins_counter += coins // 200
coins %= 200
coins_counter += coins // 100
coins %= 100
coins_counter += coins // 50
coins %= 50
coins_counter += coins // 20
coins %= 20
coins_counter += coins // 10
coins %= 10
coins_counter += coins // 5
coins %= 5
coins_counter += coins // 2
coins %= 2
if coins == 1:
    coins_counter += 1

print(int(coins_counter))
