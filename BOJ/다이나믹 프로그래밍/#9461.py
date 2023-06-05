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

# 규칙 찾아서
T = int(input())
P = [0]* 101
P[1] = 1
P[2] = 1
P[3] = 1
P[4] = 2
P[5] = 2
P[6] = 3
P[7] = 4
P[8] = 5
P[9] = 7

for i in range(10, 101):
    P[i] = P[i-1] + P[i-5]

for _ in range(T):
    N = int(input())
    print(P[N])