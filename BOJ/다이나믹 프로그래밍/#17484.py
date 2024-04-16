import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

direction = [-1, 0, 1]

def dfs(col, row, depth, before, answer):
    if col == N-1:
        return min(answer, temp)
    for i in direction:
        if i != before:
            temp = dfs(col+1, row+i, i, answer + graph[col+1][row+i])
    return low
