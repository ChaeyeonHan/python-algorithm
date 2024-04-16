import sys
from collections import deque
input = sys.stdin.readline

def bfs(x, y, graph, team):
    queue = deque()  # 시작점
    queue.append((x, y))
    graph[x][y] = 0  # 방문처리
    count = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= M or ny < 0 or ny >= N:
                continue
            if graph[nx][ny] == team:
                graph[nx][ny] = 0
                queue.append((nx, ny))
                count += 1

    return count*count

N, M = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(M)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

white, blue = 0, 0
for i in range(M):
    for j in range(N):
        if graph[i][j] == 'W':
            white += bfs(i, j, graph, 'W')
        if graph[i][j] == 'B':
            blue += bfs(i, j, graph, 'B')
print(white, blue)