price = int(input())
money = 1000 - price

coins = [500, 100,  50, 10, 5, 1]
count = 0
for coin in coins:
    count += money // coin
    money %= coin

print(count)