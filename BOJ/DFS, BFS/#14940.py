# 시간초과
# import sys
# from collections import deque
# input = sys.stdin.readline
# N, M = map(int, input().split())
# graph = []
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]
#
# for i in range(N):
#     array = list(map(int, input().split()))
#     for j in range(M):
#         if array[j] == 2:
#             x, y = i, j
#     graph.append(array)
#
# def find_distance(x1, y1, x2, y2):  # 시작점, 2번 위치(x1, y1)에서 끝점(x2, y2) 최단거리 구하기
#     queue = deque()
#     queue.append([x1, y1])  # 2번 위치(시작점) 넣어주기
#     visited = [[False]*N for _ in range(M)]
#
#     if graph[x2][y2] == 0 or graph[x2][y2] == 2:
#         return 0
#     while queue:
#         a, b = queue.popleft()
#         if a == x2 and b == y2:
#             return visited[a][b]
#
#         for i in range(4):
#             nx = a + dx[i]
#             ny = b + dy[i]
#             if nx < 0 or nx >= N or ny < 0 or ny >= M:  # 범위를 벗어난 경우
#                 continue
#             if graph[nx][ny] == 1 and visited[nx][ny] == 0:  # 이동가능하고 아직 방문 안한경우
#                 queue.append([nx, ny])
#                 visited[nx][ny] = visited[a][b] + 1
#
#     return -1
#
# for i in range(N):
#     for j in range(M):
#         print(find_distance(x, y, i, j), end=' ')
#     print()

import sys
from collections import deque
input = sys.stdin.readline
N, M = map(int, input().split())
graph = []

for _ in range(N):
    graph.append(list(map(int, input().split())))

visited = [[-1]*M for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(i, j):
    queue = deque()
    queue.append([i, j])

    visited[i][j] = 0

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if graph[nx][ny] == 0 and visited[nx][ny] == -1:  # 그래프에서 0이면, 방문 X
                visited[nx][ny] = 0  # 방문불가 처리
            elif graph[nx][ny] == 1 and visited[nx][ny] == -1:
                visited[nx][ny] = visited[x][y] + 1
                queue.append([nx, ny])

for i in range(N):
    for j in range(M):
        if graph[i][j] == 2 and visited[i][j] == -1:  # 목표지점에서
            bfs(i, j)

for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            print(0, end=' ')
        else:
            print(visited[i][j], end=' ')
    print()
