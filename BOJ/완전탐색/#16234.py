import sys
from collections import deque
input = sys.stdin.readline

N, L, R = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    q = deque()
    tmp = []
    q.append((x, y))
    tmp.append((x, y))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0:
                if L <= abs(graph[nx][ny] - graph[x][y]) <= R:  # L<=인구차이<=R 라면 국경 열어준다
                    visited[nx][ny] = 1
                    q.append((nx, ny))
                    tmp.append((nx, ny))

    return tmp

result = 0
while True:
    visited = [[0] * (N + 1) for _ in range(N + 1)]
    flag = 0  # 국경선이 열렸는지 표시
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                visited[i][j] = 1
                unit = bfs(i, j)
                if len(unit) > 1:  # 국경선이 열린경우
                    flag = 1
                    num = sum([graph[x][y] for x, y in unit]) // len(unit)
                    for x, y in unit:  # 연합 인구수 업데이트
                        graph[x][y] = num

    if flag == 0:
        break
    result += 1

print(result)