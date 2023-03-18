import sys
input = sys.stdin.readline

N, K = map(int, input().split())
coins = []
for _ in range(N):
    coins.append(int(input()))
cnt = 0
coins.sort(reverse=True)

for coin in coins:
    if K >= coin:
        cnt += K // coin
        K = K % coin

print(cnt)
