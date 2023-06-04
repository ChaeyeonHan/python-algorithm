import sys
input = sys.stdin.readline

T = int(input())
P = [0]* (101)
P[1] = 1
P[2] = 1
P[3] = 1

for i in range(3, 101):
    P[i] = P[i-3] + P[i-2]

for _ in range(T):
    N = int(input())
    print(P[N])