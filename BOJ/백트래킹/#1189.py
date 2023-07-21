import sys
input = sys.stdin.readline

R, C, K = map(int, input().split())
graph = [list(input().rstrip()) for i in range(R)]

# print(graph)  # [['.', '.', '.', '.'], ['.', 'T', '.', '.'], ['.', '.', '.', '.']]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

cnt = 0
def dfs(x, y, count):
    global cnt
    if (x == 0 and y == C-1) and count == K:
        cnt += 1
    else:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (0 <= nx < R and 0 <= ny < C) and graph[nx][ny] == '.':
                graph[nx][ny] = 'T'
                dfs(nx, ny, count+1)
                graph[nx][ny] = '.'


graph[R-1][0] = 'T'  # 시작지점 방문처리
dfs(R-1, 0, 1)
print(cnt)