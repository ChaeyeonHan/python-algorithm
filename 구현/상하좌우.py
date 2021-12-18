N = int(input())
x, y = 1, 1
plans = input().split()  # 어떻게 움직일 것인지 입력받음
#   서, 동, 북, 남
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

move_types = ['L', 'R', 'U', 'D']

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    if nx < 1 or ny < 1 or nx > N or ny > N:  # 범위를 벗어난 경우
        continue
    x, y = nx, ny

print(x, y)