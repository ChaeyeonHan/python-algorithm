import sys
from collections import deque
input = sys.stdin.readline
INF = int(1e9)

def bfs(start):
    # 최소 시간, 방법의 수
    sec, num = INF, 0

    queue = deque()
    queue.append((start, 0))   # 현재 위치, 횟수

    while queue:
        x, time = queue.popleft()
        visited[x] = True
        if x == K:  # 도착지점이면
            if time < sec:
                sec = time
                num = 1
            elif time == sec:
                num += 1
            continue

        for pos in (x-1, x+1, 2*x):
            if 0 <= pos <= 100000:
                if not visited[pos]:
                    queue.append((pos, time+1))
    return sec, num


N, K = map(int, input().split())
visited = [0] * 100001

a, b = bfs(N)
print(a)
print(b)