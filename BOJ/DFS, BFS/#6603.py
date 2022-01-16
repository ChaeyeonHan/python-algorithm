import sys
from itertools import combinations

while True:  # 0이 입력되기 전까지
    S = list(map(int, sys.stdin.readline().split()))
    if S[0] == 0:
        break
    del S[0]
    nums = combinations(S, 6)
    for i in nums:
        for j in i:
            print(j, end=' ')
        print()
    print()