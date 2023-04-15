import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())
visited = [-1] * 100001

def find(target):  # 동생 위치가 target
    queue = deque([N])
    visited[N] = 0
    while queue:
        x = queue.popleft()
        if x == target:
            return visited[target]
        for pos in [x + 1, x - 1, x * 2]:
            if 0 <= pos < 100001 and visited[pos] == -1:  # 해당 위치가 범위 내에 있고 아직 방문 전이면
                if pos == x * 2:  # 순간이동 한 경우
                    visited[pos] = visited[x]
                    queue.appendleft(pos)  # 순간이동 먼저 탐색하도록
                else:  # 걸은 경우
                    visited[pos] = visited[x] + 1
                    queue.append(pos)

print(find(K))
