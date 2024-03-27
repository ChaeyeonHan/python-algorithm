import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 덩어리 구하는 함수
def count_ice(graph):
    visited = [[0]*M for _ in range(N)]
    queue = deque()
    cnt = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] != 0 and not visited[i][j]:
                queue.append((i, j))
                visited[i][j] = True
                while queue:
                    x, y = queue.popleft()
                    for k in range(4):
                        nx, ny = x+dx[k], y+dy[k]
                        if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] != 0:
                            if not visited[nx][ny]:
                                queue.append((nx, ny))
                                visited[nx][ny] = True
                cnt += 1
    return cnt

# 1년동안 빙산 녹는 함수
def melt(graph):
    visited = [[0]*M for _ in range(N)]
    temp = [[0]*M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if graph[i][j] != 0:
                sea_cnt = 0  # 주변바다 갯수 카운트
                for k in range(4):
                    nx, ny = i+dx[k], j+dy[k]
                    if 0 <= nx < N and 0 <= ny < M:
                        if graph[nx][ny] == 0:
                            sea_cnt += 1
                temp[i][j] = max(0, graph[i][j]-sea_cnt)
    return temp

year = 0
while True:
    graph = melt(graph)
    result = count_ice(graph)
    year+=1
    if result >= 2:
        break
    elif result == 0:  #모두 다 녹은 경우
        year = 0
        break
    # year += 1

print(year)