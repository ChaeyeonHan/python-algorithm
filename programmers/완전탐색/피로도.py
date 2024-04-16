# dfs 풀이(깊이우선, 재귀사용)

answer = 0
visited = []
N = 0

def dfs(k, cnt, dungeons):
    global answer
    if cnt > answer:
        answer = cnt

    for j in range(len(dungeons)):
        if k >= dungeons[j][0] and not visited[j]:
            visited[j] = 1
            dfs(k-dungeons[j][1], cnt+1, dungeons)
            visited[j] = 0


def solution(k, dungeons):
    global N, visited
    N = len(dungeons)
    visited = [0] * N
    dfs(k, 0, dungeons)
    return answer

# 순열사용
from itertools import permutations

def solution(k, dungeons):
    answer = 0
    for p in permutations(dungeons, len(dungeons)):
        temp = k
        count = 0
        for need, spend in p:
            if temp >= need:
                temp -= spend
                count += 1
        answer = max(answer, count)
    return answer
