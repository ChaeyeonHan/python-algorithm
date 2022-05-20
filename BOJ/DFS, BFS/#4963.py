import sys
from collections import deque

dx = [0, 0, 1, 1, 1, -1, -1, -1]  # 가로, 세로, 대각선 연결시 이동가능 -> 총 8개로 잡아줘야한다
dy = [-1, 1, -1, 0, 1, -1, 0, 1]


def bfs(x, y):  # 1이 땅, 0이 바다
    queue = deque()
    queue.append([x, y])

    while queue:
        x, y = queue.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= h or ny < 0 or ny >= w:  # 범위를 벗어난 경우
                continue
            if graph[nx][ny] == 0:  # 바다인경우 -> 계속하기
                continue
            if graph[nx][ny] == 1:  # 땅인경우
                graph[nx][ny] = 0  # visited를 사용하지 않고 방문한 땅은 0으로 바꿔준다!
                queue.append([nx, ny])  # 큐에 넣어주기

while True:
    w, h = map(int, sys.stdin.readline().rstrip().split())  # 너비, 높이
    if (w == 0) and (h == 0):
        break
    graph=[]
    for _ in range(h):
        graph.append(list(map(int, sys.stdin.readline().rstrip().split())))  # 지도 입력
    # visited = [[False] * w for _ in range(h)]
    result = 0
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1:  #1(육지)이면
                result += 1
                bfs(i, j)
    print(result)