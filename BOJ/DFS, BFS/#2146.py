import sys
from collections import deque
input = sys.stdin.readline

# 섬에 각각 번호 부여(구분)
def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    graph[x][y] = count

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and graph[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                graph[nx][ny] = count
                queue.append((nx, ny))


# 최소거리 구하기
def bfs_island(num):
    global answer
    distance = [[-1]*N for _ in range(N)]
    queue = deque()

    for i in range(N):
        for j in range(N):
            if graph[i][j] == num:
                queue.append((i, j))
                distance[i][j] = 0

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            # 다른 섬을 만나면 기존 이동거리와 비교해서 짧은 거리 선택
            if graph[nx][ny] != num and graph[nx][ny] != 0:
                answer = min(answer, distance[x][y])
                return

            # 바다를 만나면 거리 +1 (바다&아직 방문하지 않은 경우)
            if graph[nx][ny] == 0 and distance[nx][ny] == -1:
                distance[nx][ny] = distance[x][y] + 1
                queue.append((nx, ny))


# 1이 육지, 0이 바다
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]
count = 1
answer = sys.maxsize

for i in range(N):
    for j in range(N):
        if not visited[i][j] and graph[i][j] == 1:
            bfs(i, j)
            count += 1

# 섬의 갯수만큼 순회
for i in range(1, count):
    bfs_island(i)

print(answer)