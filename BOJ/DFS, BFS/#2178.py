from collections import deque

N, M = map(int, input().split())
matrix=[]
for i in range(N):
    matrix.append(list(map(int, input())))
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


# bfs를 사용하면 효율적으로 풀수 있음 -> 시작지점부터 순차적으로 모든 노드 탐색
def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):  # 현재위치에서 동서남북 네방향 모두 확인
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue
            if matrix[nx][ny] == 0:
                continue
            if matrix[nx][ny] == 1:
                matrix[nx][ny] = matrix[x][y] + 1
                queue.append((nx, ny))
    return matrix[N-1][M-1]

print(bfs(0, 0))