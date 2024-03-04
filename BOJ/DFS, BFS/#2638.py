import sys
from collections import deque

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    queue = deque()
    queue.append((0, 0))  # 공기
    visited[0][0] = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 0:
                if graph[nx][ny] >= 1:  # 치즈
                    graph[nx][ny] += 1
                else:
                    visited[nx][ny] = 1
                    queue.append((nx, ny))

time = 0
while True:
    visited = [[0] * M for _ in range(N)]
    bfs()
    flag = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] >= 3:  # 3이 되면 녹는다
                graph[i][j] = 0
                flag = 1
            elif graph[i][j] == 2:
                graph[i][j] = 1

    if flag == 1:
        time += 1
    else:  # 녹을 치즈가 없는 경우
        break

print(time)
