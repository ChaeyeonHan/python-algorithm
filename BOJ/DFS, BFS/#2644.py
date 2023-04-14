# dfs 풀이
import sys
input = sys.stdin.readline

n = int(input())
a, b = map(int, input().split())
m = int(input())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

visited = [0] * (n+1)
result = [0] * (n+1)  # 7번과 다른 모든 사람들과의 촌수를 다 저장하는 리스트

def dfs(v):
    visited[v] = True
    for i in graph[v]:  # graph = [[], [2, 3], [1, 7, 8, 9], [1], [5, 6] ..]
        if not visited[i]:
            result[i] = result[v] + 1
            dfs(i)
dfs(a)
if result[b] > 0:
    print(result[b])
else:
    print(-1)


# bfs 풀이
from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
a, b = map(int, input().split())
m = int(input())

graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)
result = [0] * (n+1)

for i in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)


def bfs(v):
    queue = deque([v])
    visited[v] = True

    while queue:
        k = queue.popleft()

        for i in graph[k]:
            if not visited[i]:
                visited[i] = True
                result[i] = result[k] + 1
                queue.append(i)

bfs(a)
print(result[b] if result[b] > 0 else -1)