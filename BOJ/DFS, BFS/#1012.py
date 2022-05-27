import sys
from collections import deque
dx=[0, 0, -1, 1]
dy=[-1, 1, 0, 0]

def bfs(graph, x, y):
    queue = deque()
    queue.append((x, y))
    graph[x][y] = 0  # 지나간거 표시해주기

    while queue:   # 큐가 빌때까지
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or nx >=N or ny<0 or ny >= M:  # 범위 벗어난 경우
                continue
            if graph[nx][ny] == 1:
                queue.append((nx, ny))
                graph[nx][ny] = 0


T = int(sys.stdin.readline().rstrip())  # 테스트 케이스의 갯수

while T:
    M, N, K = map(int, sys.stdin.readline().rstrip().split())  # 가로, 세로, 위치의 갯수
    area=[[0] * M for i in range(N)]
    result = 0
    for _ in range(K):  # 배추의 위치가 한개씩 모두 주어진다
        a, b = map(int, sys.stdin.readline().rstrip().split())
        # area[a][b] = 1
        area[b][a] = 1
    for i in range(N):
        for j in range(M):
            if area[i][j] == 1:
                result += 1
                bfs(area, i, j)
    print(result)
    T -= 1


# M, N = map(int, input().split())  # 5, 7
# area = [M * [0] for i in range(N)]
# print(area)
# [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]