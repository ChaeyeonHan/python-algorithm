import sys
input = sys.stdin.readline

N = int(input())
dx = [-1, 0, 1, 0]  # 북동남서 순으로
dy = [0, 1, 0, -1]
moves = input().rstrip()

x, y = 0, 0  # 홍준이 초기 위치
dir = 2  # 방향 남쪽
graph = [[0, 0]]  # 이동한 좌표 저장
for move in moves:
    if move == 'L':  # 방향만 이동
        dir = (dir-1)%4
    if move == 'R':
        dir = (dir+1)%4
    if move == 'F':
        x += dx[dir]
        y += dy[dir]
        graph.append([x, y])

# graph의 가장 큰값, 작은값 차이로 행과 열의 크기 구하기
N = max(graph)[0]-min(graph)[0]+1
M = max(graph, key=lambda x:x[1])[1]-min(graph, key=lambda x:x[1])[1]+1

# [0,0]에서 시작했으므로 음수/양수 좌표 섞여있음 => 모두 양수좌표로 이동시킨다
min_x = min(graph, key=lambda x:x[0])[0]
min_y = min(graph, key=lambda x:x[1])[1]
for i in graph:
    i[0] += abs(min_x)
    i[1] += abs(min_y)

maps = [[False]*M for _ in range(N)]
for i in graph:
    maps[i[0]][i[1]] = "."

for i in range(N):
    for j in range(M):
        if maps[i][j] == False:
            maps[i][j] = "#"

for row in maps:
    for i in range(len(row)):
        print(row[i], end='')
    print("")