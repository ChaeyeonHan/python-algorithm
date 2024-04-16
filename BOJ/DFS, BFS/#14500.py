import sys
input = sys.stdin.readline

def dfs(x, y, depth, total):
    global answer
    if answer >= total + max_value*(4-depth):
        return
    if depth == 4:  # 4칸을 모두 돌면
        answer = max(total, answer)
        return
    else:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 0:
                if depth == 2:  # ㅗ 모양
                    visited[nx][ny] = 1
                    dfs(x, y, depth+1, total+graphs[nx][ny])
                    visited[nx][ny] = 0
                visited[nx][ny] = 1
                dfs(nx, ny, depth+1, total+graphs[nx][ny])
                visited[nx][ny] = 0


N, M = map(int, input().split())
graphs = [list(map(int, input().split())) for _ in range(N)]
dx = [-1, 0, 1, 0]  # 북 동 남 서
dy = [0, 1, 0, -1]
visited = [[False] * M for _ in range(N)]

answer = 0
max_value = max(map(max, graphs))  # 모든 좌표중 최댓값
for i in range(N):
    for j in range(M):
        visited[i][j] = 1
        dfs(i, j, 1, graphs[i][j])
        visited[i][j] = 0
print(answer)