import sys
input = sys.stdin.readline

N, K = map(int, input().split())
graph = []  # 체스판 정보
horse = []  # 말 정보
chess = [[[] for _ in range(N)] for _ in range(N)]  # 말의 위치를 담은 체스판의 정보

dx = [0, 0, -1, 1]  # 동서북남
dy = [1, -1, 0, 0]

for _ in range(N):  # 0 흰색, 1 빨간색, 2 파란색
    graph.append(list(map(int, input().split())))

for i in range(K):
    x, y, dir = map(int, input().split())
    horse.append([x-1, y-1, dir-1])  # 말의 정보 : 열, 행, 이동방향
    # 1 오, 2 왼, 3 위, 4 아래 => (저장) 0 오, 1 왼, 2 위, 3 아래
    chess[x-1][y-1].append(i)

def change_dir(d):
    if d in [0, 2]:
        d += 1
    elif d in [1, 3]:
        d -= 1
    return d

def move(number):  # 말의 번호를 통해 움직이는 함수
    x, y, dir = horse[number]
    nx = x + dx[dir]
    ny = y + dy[dir]
    if (nx < 0 or nx >= N or ny < 0 or ny >= N) or graph[nx][ny] == 2:  # 범위를 벗어나거나 이동하려는 칸이 파란색이면
        dir = change_dir(dir)
        horse[number][2] = dir
        nx = x + dx[dir]
        ny = y + dy[dir]
        if (nx < 0 or nx >= N or ny < 0 or ny >= N) or graph[nx][ny] == 2:
            return True  # 방향 바꾸고 나서 또 다시 범위를 벗어나거나 파란색이면 이동X
    # 이동하기 전에, 현재 말의 번호 정보 저장
    horse_append = []
    for idx, h_number in enumerate(chess[x][y]):  # 현재위치에 있는 말을 꺼내면서 number 찾으면
        if h_number == number:
            horse_append.extend(chess[x][y][idx:])  # 현재 말 위에 있는 모든 말 저장
            chess[x][y] = chess[x][y][:idx]
            break

    if graph[nx][ny] == 1:  # 빨간색이면
        horse_append = horse_append[-1::-1]

    for h in horse_append:  # horse 리스트에 이동한 말의 위치 저장
        horse[h][0], horse[h][1] = nx, ny
        chess[nx][ny].append(h)

    if len(chess[nx][ny]) >= 4:  # 말이 4개가 되면 종료
        return False
    return True

cnt = 0  # 게임 턴 횟수
while True:
    flag = False
    if cnt > 1000:
        print(-1)
        break
    for i in range(K):
        if move(i) == False:
            flag = True
            break
    cnt += 1
    if flag:
        print(cnt)
        break
