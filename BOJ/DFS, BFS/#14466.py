import sys
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(r1, c1):
    queue = deque()
    queue.append((r1, c1))
    cow_visit[r1][c1] = True

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if cow_visit[nx][ny]:
                continue
            if (nx, ny) in road[x][y]:  # 다리인 경우
                continue
            cow_visit[nx][ny] = True
            queue.append((nx, ny))

N, K, R = map(int, input().split())

# 길 입력받기
road = [[[] for _ in range(N)] for _ in range(N)]
for _ in range(R):
    r1, c1, r2, c2 = map(int, input().split())
    road[r1-1][c1-1].append((r2-1, c2-1))
    road[r2-1][c2-1].append((r1-1, c1-1))

# cows = [list(map(int, input().split())) for _ in range(K)]
cows = []
for _ in range(K):
    a, b = map(int, input().split())
    cows.append((a-1, b-1))

result = 0
# 한마리씩 확인하며 방문여부 탐색
for i, cow in enumerate(cows):
    cow_visit = [[False]*N for _ in range(N)]
    # 현재 소가 길 없이 탐색하는 경우 저장
    bfs(cow[0], cow[1])
    for r2, c2 in cows[i+1:]:
        if not cow_visit[r2][c2]:  # 방문하지 못하는 경우
            result += 1

print(result)