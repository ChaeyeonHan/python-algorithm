import sys
from itertools import combinations

input = sys.stdin.readline

N = int(input())
array = []

for _ in range(N):
    array.append(list(map(int, input().split())))

result = 1e9
for i in range(1, N+1):
    for comb in combinations(array, i):
        sour, bitter = 1, 0
        for k in comb:
            sour *= k[0]
            bitter += k[1]
        result = min(result, abs(sour-bitter))

print(result)