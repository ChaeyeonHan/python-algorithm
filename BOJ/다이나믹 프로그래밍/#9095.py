import sys
input = sys.stdin.readline

d = [0] * 11  # n은 11보다 작음

d[1] = 1
d[2] = 2
d[3] = 4

for i in range(4, 11):  # 4부터 10까지
    d[i] = sum(d[i-3:i])  # i-3번째부터 i-1번째까지 더한 값

T = int(input())
for _ in range(T):
    print(d[int(input())])

