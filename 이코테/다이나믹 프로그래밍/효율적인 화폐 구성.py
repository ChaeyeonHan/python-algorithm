import sys
n, m = map(int, sys.stdin.readline().rstrip().split())
coins=[]
for i in range(n):
    coins.append(int(input()))

d = [10001] * (m+1)

d[0] = 0
for i in range(n):
    for j in range(coins[i], m+1):
        if (d[j - coins[i]]) != 10001:
            d[j] = min(d[j], d[j-coins[i]] + 1)

if d[n] == 10001:
    print(-1)  # m원을 만들지 못하는 경우
else:
    print(d[m])