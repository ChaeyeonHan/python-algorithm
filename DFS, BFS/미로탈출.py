from collections import deque
N, M = map(int, input().split())

graph = []
for i in range(N):
    graph.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


# 1은 이동가능, 시작위치는 (1,1)로 고정 최소가 되게끔
def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    while queue:  # 큐가 빌때까지 반복
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:   #범위를 벗어난경우
                continue
            if graph[nx][ny] == 0:  # 벽인경우는 무시
                continue
            if graph[nx][ny] == 1:  #이동가능한 경우
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    return graph[N-1][M-1]

print(bfs(0, 0))



