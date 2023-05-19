import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
dp = [1] * 1001

for i in range(n):
    for j in range(i):
        if nums[i] > nums[j]:
            dp[i] = max(dp[j]+1, dp[i])
print(max(dp))