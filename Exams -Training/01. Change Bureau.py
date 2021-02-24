number_bitcoin = int(input())
number_chinese_yuan = float(input())
commission = float(input())
one_euro = 1.95
one_dollar_to_euro = 1.76 / 1.95
one_chinese_yuan_to_euro = 0.15 * 1.76 / 1.95
one_bitcoin_to_euro = 1168 / 1.95
total_money = (number_bitcoin * one_bitcoin_to_euro + number_chinese_yuan * one_chinese_yuan_to_euro) * (100 - commission) / 100
print(f"{total_money:.2f}")
