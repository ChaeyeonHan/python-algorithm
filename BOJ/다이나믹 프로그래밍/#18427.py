import sys
input = sys.stdin.readline

N, M, H = map(int, input().split())
dp = [[1] + [0]*H for _ in range(N+1)]  # 0을 만드는 경우는 1가지

for i in range(1, N+1):
    dp[i] = dp[i-1].copy()
    blocks = list(map(int, input().split()))
    for b in blocks:
        for j in range(b, H+1):
            dp[i][j] += dp[i-1][j-b]

print(dp[N][H]%10007)
