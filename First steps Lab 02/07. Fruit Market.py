strawberries_price = float(input())
bananas_quantity = float(input())
oranges_quantity = float(input())
raspberries_quantity = float(input())
stawberries_quantity = float(input())
raspberries_price = strawberries_price / 2
oringes_price = raspberries_price * 0.6
bananas_price = raspberries_price * 0.2
needed_money = strawberries_price * stawberries_quantity + raspberries_price * raspberries_quantity + oringes_price * oranges_quantity + bananas_price * bananas_quantity
print(needed_money)