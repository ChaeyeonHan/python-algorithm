import sys
from collections import deque
input = sys.stdin.readline


def bfs(start):
    queue = deque()
    queue.append(start)
    visited[start] = True
    while queue:
        curr = queue.popleft()
        for next in graph[curr]:
            if not visited[next]:
                queue.append(next)
                visited[next] = True


N = int(input())
M = int(input())
g = [list(map(int, input().split())) for _ in range(N)]
graph = [[] for _ in range(N)]

for i in range(N):
    for j in range(N):
        if g[i][j] == 1:
            graph[i].append(j)

visited = [False for _ in range(N)]
plan = list(map(int, input().split()))

bfs(plan[0]-1)
answer = True

for i in plan:
    if not visited[i-1]:
        answer = False
        break
if answer:
    print("YES")
else:
    print("NO")