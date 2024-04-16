# 정점의 갯수

def dfs(x, cnt):
    global result
    visited[x] = True
    for i in graph[x]:
        if visited[i] == 0:
            visited[i] = True
            dfs(i, cnt+1)
    visited[x] = 0
    if cnt > result:
        result = cnt

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    result = 0
    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    for i in range(1, N+1):  # 시작점을 변경하면서 그래프 방문
        visited = [0 for _ in range(N+1)]
        dfs(i, 1)
    print(f'#{t} {result}')