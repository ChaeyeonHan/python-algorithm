import sys
from itertools import combinations

while True:
    S = list(map(int, input().split()))

    if S[0] == 0:
        break
    del S[0]
    case = combinations(S, 6)
    # print(list(case))  # [(1, 2, 3, 4, 5, 6), (1, 2, 3, 4, 5, 7), (1, 2, 3, 4, 6, 7), (1, 2, 3, 5, 6, 7), (1, 2, 4, 5, 6, 7), (1, 3, 4, 5, 6, 7), (2, 3, 4, 5, 6, 7)]
    for i in case:
        for j in i:
            print(j, end=' ')
        print()
    print()