import sys
input = sys.stdin.readline

R, C = map(int, input().split())
graph = []
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
alpha = set()

for _ in range(R):
    graph.append(list(input().rstrip()))

result = 0
def findAlpha(x, y, cnt):
    global result
    result = max(result, cnt)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < R and 0 <= ny < C:
            if graph[nx][ny] not in alpha:  # 집합에 없으면
                alpha.add(graph[nx][ny])
                findAlpha(nx, ny, cnt+1)
                alpha.remove(graph[nx][ny])

alpha.add(graph[0][0])
findAlpha(0, 0, 1)  # 좌측상단에서 시작
print(result)