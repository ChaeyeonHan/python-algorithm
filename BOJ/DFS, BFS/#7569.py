import sys
from collections import deque
input = sys.stdin.readline

# 3차원 배열
M, N, H = map(int, input().split())
tomatoes = []
queue = deque()  # 익은 토마토 좌표 모두 저장
for i in range(H):
    array = []
    for j in range(N):
        array.append(list(map(int, input().split())))
        for k in range(M):
            if array[j][k] == 1:  # 익은 토마토이면
                queue.append((i, j, k))
    tomatoes.append(array)

# print(tomatoes)
dx = [-1, 1, 0, 0, 0, 0]  # 상하좌우 + 상자 위아래
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

while queue:
    x, y, z = queue.popleft()
    for i in range(6):
        nx = x + dx[i]
        ny = y + dy[i]
        nz = z + dz[i]
        if nx < 0 or nx >= H or ny < 0 or ny >= N or nz < 0 or nz >= M:  # 범위를 벗어난 경우
            continue
        if tomatoes[nx][ny][nz] == 0:  # 익지 않은 토마토이면
            tomatoes[nx][ny][nz] = tomatoes[x][y][z] + 1  # 하루+1
            queue.append((nx, ny, nz))

days = 0
for i in range(H):
    for j in range(N):
        for k in range(M):
            if tomatoes[i][j][k] == 0:  # 익지 않은 토마토 있으면
                print(-1)
                exit(0)  # 프로그램 전체 종료(breakX)
            days = max(days, tomatoes[i][j][k])
print(days-1)