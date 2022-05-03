N, M = map(int, input().split())
x, y, direction = map(int, input().split())

# 맵을 생성하여 0으로 초기화***
d = [[0]*M for _ in range(N)]
d[x][y] = 1  #현재위치 방문처리

# 맵정보 입력받기 0은 육지, 1은 바다
array = []
for i in range(N):
    array.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]  # 북동남서 방향
dy = [0, 1, 0, -1]

# 왼쪽으로 회전
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

count = 1
turn_time = 0
while True:
    turn_left()  # 방향회전
    nx = x + dx[direction]
    ny = y + dy[direction]
    if d[nx][ny] == 0 and array[nx][ny] == 0:  # 방문하지 않았고 육지인경우 이동
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    else:
        turn_time += 1

    if turn_time == 4:  # 네방향 모두 이동불가능한 경우, 뒤로 이동
        nx = x - dx[direction]
        ny = y - dy[direction]
        if array[nx][ny] == 0:  # 뒤로 이동 가능한 경우
            x = nx
            y = ny
        else:
            break
        turn_time = 0

print(count)