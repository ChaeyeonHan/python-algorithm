import sys
input = sys.stdin.readline

N = int(input())
consults = []
consults = [list(map(int, input().split())) for _ in range(N)]  # [소요시간, 금액]

dp = [0]*(N+1)
for i in range(1, N+1):
    t, p = consults[i-1][0], consults[i-1][1]
    dp[i] = max(dp[i], dp[i-1])
    fin_date = i + t-1
    if fin_date < N+1:
        dp[fin_date] = max(dp[fin_date], dp[i-1]+p)
    print(*dp)

# print(*dp)
print(dp[N])