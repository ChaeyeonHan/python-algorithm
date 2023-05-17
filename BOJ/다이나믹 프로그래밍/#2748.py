import sys
input = sys.stdin.readline

n = int(input())

d = [0] * 91
d[0] = 0
d[1] = 1

def fibo(n):
    for i in range(2, n+1):
        d[i] = d[i-1] + d[i-2]
    return d[n]

print(fibo(n))