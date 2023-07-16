import sys
input = sys.stdin.readline

N, M = map(int, input().split())

total = 0
prices = []  # 6개의 가격, 낱개 가격
for _ in range(M):
    a, b = map(int, input().split())
    prices.append([a, b])

package_prices = sorted(prices, key=lambda x: x[0])
one_prices = sorted(prices, key=lambda x: x[1])

if package_prices[0][0] < one_prices[0][1] * 6:  # 낱개로 6개 사는것보다 패키지 가격이 저렴한 경우
    total = package_prices[0][0] * (N // 6) + one_prices[0][1] * (N % 6)

    if package_prices[0][0] < one_prices[0][1] * (N % 6):
        total = package_prices[0][0] * (N // 6 + 1)  # 패키지 하나 더 구매

else:
    total = one_prices[0][1] * N
print(total)