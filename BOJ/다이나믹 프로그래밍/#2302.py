import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
seats = [int(input()) for _ in range(M)]

dp = [0]*(N+1)
dp[0] = 1
dp[1] = 1
for i in range(2, N+1):
    dp[i] = dp[i-1] + dp[i-2]

result = 1
k = 0
for i in range(len(seats)):
    gap = seats[i]-k-1
    # print("gap: " + str(gap))
    result *= dp[gap]
    k = seats[i]
result *= dp[N-k]

print(result)