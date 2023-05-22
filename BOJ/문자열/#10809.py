import sys
input = sys.stdin.readline

S = input().rstrip()
alpha = 'abcdefghijklmnopqrstuvwxyz'

for i in alpha:
    if i in S:
        # print(S.find(i), end=' ')
        print(S.index(i), end=' ')
    else:
        print(-1, end=' ')