import sys
from collections import deque
input = sys.stdin.readline

# 상하좌우 이동
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(i, j, graph, costs):
    q = deque([(i, j)])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if costs[nx][ny] > costs[x][y] + graph[nx][ny]:
                    costs[nx][ny] = costs[x][y] + graph[nx][ny]
                    q.append((nx, ny))

i = 1
while True:
    N = int(input())
    if N == 0:
        break
    graph = [list(map(int, input().split())) for _ in range(N)]
    costs = [[int(1e9)] * N for _ in range(N)]
    costs[0][0] = graph[0][0]

    bfs(0, 0, graph, costs)
    print(f'Problem {i}: {costs[N-1][N-1]}')
    i += 1