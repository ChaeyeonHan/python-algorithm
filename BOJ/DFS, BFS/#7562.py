from collections import deque
import sys

dx=[2, 2, 1, 1, -1, -1, -2, -2]
dy=[1, -1, 2, -2, 2, -2, 1, -1]

def bfs(x_pos, y_pos, x, y):
    queue = deque()
    queue.append((x, y))
    area[x][y] = 1  # 1로 바꿔주기
    while queue:
        x, y = queue.popleft()
        if x == x_pos and y == y_pos:
            print(area[x][y]-1)
            return
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < L and 0 <= ny < L and area[nx][ny] == 0:  # 범위에 맞고, 아직 안지나온 점이면
                queue.append((nx, ny))
                area[nx][ny] = area[x][y] + 1  # 기존 좌표(횟수)에 더하는 방식으로


T = int(sys.stdin.readline().rstrip())
while T:
    L = int(sys.stdin.readline().rstrip())
    area=[[0]*L for _ in range(L)]
    x_pos, y_pos = map(int, sys.stdin.readline().rstrip().split())  # 현재 위치
    x, y = map(int, sys.stdin.readline().rstrip().split())  # 이동하려는 칸
    bfs(x_pos, y_pos, x, y)
    T -= 1