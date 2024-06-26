import sys
input = sys.stdin.readline

N = int(input())
dp = []
for _ in range(N):
    dp.append(list(map(int, input().split())))

for i in range(1, N):  # 두번째 층부터 시작
    for j in range(i+1):
        if j == 0:
            dp[i][j] = dp[i][j] + dp[i-1][j]
        elif j == i:
            dp[i][j] = dp[i][j] + dp[i-1][j-1]
        else:
            dp[i][j] = dp[i][j]+max(dp[i-1][j-1], dp[i-1][j])

print(max(dp[N-1]))