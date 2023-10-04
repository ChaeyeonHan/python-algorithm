import sys
from collections import deque
input = sys.stdin.readline
# 벽을 부셨는지 여부 체크 -> visited를 3차원 배열로 만들어서 방문여부랑 같이 저장

N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().rstrip())))
visited = [[[0, 0] for _ in range(M)] for _ in range(N)]
# [[[0, 0], [0, 0], [0, 0]], [[0, 0], [0, 0], [0, 0]], [[0, 0], [0, 0], [0, 0]], [[0, 0], [0, 0], [0, 0]]]

# 상하좌우 이동
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(x, y, z):
    queue = deque()
    queue.append([x, y, z])  # (0, 0, 0)에서 시작
    visited[x][y][z] = 1

    while queue:
        x, y, z = queue.popleft()

        if x == N-1 and y == M-1:  # 끝지점에 도착
            return visited[x][y][z]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:  # 범위를 벗어난 경우
                continue
            # 현재 위치가 벽이 아니고(이동 가능한 경우), 아직 방문하지 않았다면
            if graph[nx][ny] == 0 and visited[nx][ny][z] == 0:
                visited[nx][ny][z] = visited[x][y][z] + 1
                queue.append([nx, ny, z])
            # 벽을 부수는 경우(현재 위치가 벽이고, 벽을 아직 부수지 않았다면)
            elif graph[nx][ny] == 1 and z == 0:
                visited[nx][ny][z+1] = visited[x][y][z] + 1
                queue.append([nx, ny, z+1])

    return -1

print(bfs(0, 0, 0))