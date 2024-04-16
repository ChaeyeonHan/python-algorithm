import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    queue = deque()
    queue.append((home[0], home[1]))
    while queue:
        x, y = queue.popleft()
        if abs(x-festival[0]) + abs(y-festival[1]) <= 1000:  # 종료조건
            print("happy")
            return
        for i in range(N):
            if abs(x-stores[i][0]) + abs(y-stores[i][1]) <= 1000 and not visited[i]:
                queue.append((stores[i][0], stores[i][1]))
                visited[i] = True
    print("sad")
    return


T = int(input())
for i in range(T):
    N = int(input())
    home = list(map(int, input().split()))
    stores = []
    for _ in range(N):
        stores.append(list(map(int, input().split())))
    festival = list(map(int, input().split()))
    visited = [False for _ in range(N+1)]
    bfs()