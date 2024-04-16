import sys
from collections import deque

N = int(input())
graph = []
max_height = 0

for _ in range(N):
    heights = list(map(int, input().split()))
    graph.append(heights)

    for i in heights:  # 최대 높이 찾기
        if i > max_height:
            max_height = i

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, n):
    q = deque()
    q.append((x, y))
    visited[x][y] = True

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if graph[nx][ny] > n and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    q.append((nx, ny))

result = 0

# 최대 높이만큼 반복해서 안전 영역이 가장 많아지도록 하는 지점을 찾는다
for i in range(max_height):
    count = 0
    visited = [[0] * N for _ in range(N)]
    for j in range(N):
        for k in range(N):
            if graph[j][k] > i and visited[j][k] == 0:
                bfs(j, k, i)
                count += 1
    result = max(result, count)

print(result)