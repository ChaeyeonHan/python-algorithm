import sys
from itertools import permutations
input = sys.stdin.readline

# 1. itertools 사용
N = int(input())

# 순열 리스트
result = list(permutations([i for i in range(1, N+1)], N))
for p in result:
    print(*p)


# 2. 백트래킹
N = int(input())
nums = [i for i in range(1, N+1)]

temp = []
def dfs(depth):
    if depth == N:
        print(*temp)
        return

    for i in range(N):
        if nums[i] not in temp:
            temp.append(nums[i])
            dfs(depth+1)
            temp.pop()
dfs(0)