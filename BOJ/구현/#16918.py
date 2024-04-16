import sys
from collections import deque
input = sys.stdin.readline

def bomb_pos():  # 폭탄 위치 찾기
    for i in range(R):
        for j in range(C):
            if graph[i][j] == 'O':
                temp.append([i, j])

def bomb_explode():  # 폭탄 터뜨리기
    while temp:
        x, y = temp.popleft()
        graph[x][y] = '.'
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < R and 0 <= ny < C:
                graph[nx][ny] = '.'

def bomb_set():  # 폭탄 설치
    for i in range(R):
        for j in range(C):
            if graph[i][j] == '.':
                graph[i][j] = 'O'

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
R, C, N = map(int, input().split())

# graph = [list(input().rstrip()) for _ in range(R)]
graph = []
for _ in range(R):
    graph.append(list(input().rstrip()))

N -= 1
while N:
    temp = deque()
    bomb_pos()  # 폭탄 채우기 전에 이전 위치 저장

    bomb_set()  # 폭탄 설치
    N -= 1  # 설치하는데 1초 소요

    if N == 0:
        break

    bomb_explode()
    N -= 1  # 폭발하는데 1초

for i in graph:
    print("".join(i))