import sys
input = sys.stdin.readline

R, C = map(int, input().split())
graph = [input().rstrip() for _ in range(R)]

# 맨 위쪽에서 시작해서 파이프가 최대한 위로 가도록
dx = [-1, 0, 1]
dy = [1, 1, 1]
visited = [[False] * C for _ in range(R)]

def dfs(x, y):
    if y == C-1:  # 빵집에 도착한 경우(마지막 열 도착)
        return True
    for i in range(3):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < R and 0 <= ny < C:
            if not visited[nx][ny] and graph[nx][ny] == '.':  # 방문하지 않고, 건물이 아닌 경우
                visited[nx][ny] = True
                if dfs(nx, ny):
                    return True

    return False


answer = 0  # 최대 경로
for i in range(R):
    if dfs(i, 0):
        answer += 1
print(answer)