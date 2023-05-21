import sys
input = sys.stdin.readline

n = int(input())

def fibo1(n):
    if n == 1 or n == 2:
        return 1  # 코드1
    else:
        return fibo1(n-1)+fibo1(n-2)

def fibo2(n):
    dp = [0] * (n+1)
    dp[1], dp[2] = 1, 1
    cnt = 0
    for i in range(3, n+1):
        dp[i] = dp[i-2] + dp[i-1]  # 코드2
        cnt += 1
    return cnt

print(fibo1(n), fibo2(n))