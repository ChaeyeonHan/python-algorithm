import sys
from collections import deque
# 연결요소 갯수 구하기

def bfs(graph, start, visited):
    q = deque()
    q.append(start)
    visited[start] = 1

    while q:
        x = q.popleft()
        for i in graph[x]:
            if not visited[i]:
                q.append(i)
                visited[i] = 1

n, m = map(int, sys.stdin.readline().rstrip().split())
# graph = [[] * (n+1)]  # [[]]
graph = [[] for _ in range(n + 1)]

visited = [0] * (n+1)  # 방문여부 체크

for _ in range(m):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    graph[b].append(a)
    graph[a].append(b)

count=0
for i in range(1, n+1):
    if visited[i] == 0:  # 방문하지 않은경우
        bfs(graph, i, visited)
        count += 1
print(count)

# DFS 풀이
import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [0] * (N+1)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 재귀
def dfs(graph, v, visited):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

cnt = 0
for i in range(1, N+1):
    if not visited[i]:
        dfs(graph, i, visited)
        cnt += 1
print(cnt)