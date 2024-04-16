import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(map(int, input().split()) for _ in range(N))]

dp = [[0]*M for _ in range(N)]
dp[0][0] = graph[0][0]

dx = [1, 0, 0]
dy = [0, -1, 1]

for i in range(N):
    for j in range(M):
        

