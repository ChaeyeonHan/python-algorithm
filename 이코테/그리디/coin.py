# 500원, 100원, 50원, 10원. 주어진 가격을 만드는 최소의 동전의 갯수 구하기
n = 1260
count = 0

coin_types = [500, 100, 50, 10]

# //는 정수부분의 몫, %는 나머지 구하기
for coin in coin_types:
    count += n // coin
    n %= coin

print(count)