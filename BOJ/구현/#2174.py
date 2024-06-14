import sys
input = sys.stdin.readline

A, B = map(int, input().split())
N, M = map(int, input().split())
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

robots = []  # 로봇 위치
for _ in range(N):
    x, y, z = input().split()
    # x = int(x)-1
    # y = B-int(y)
    if z == 'N':
        d = 0
    if z == 'E':
        d = 1
    if z == 'S':
        d = 2
    if z == 'W':
        d = 3
    robots.append([int(x), int(y), d])

commands = []
for _ in range(M):  # 명령
    x, y, z = input().split()
    commands.append([int(x), y, int(z)])

for x, type, times in commands:  # 명령로봇, 명령종류(L, R, F), 반복횟수
    for _ in range(times):
        if type == 'L':
            robots[x-1][2] = (robots[x-1][2]-1)%4
        if type == 'R':
            robots[x-1][2] = (robots[x-1][2]+1)%4
        if type == 'F':
            cur_direction = robots[x-1][2]
            robots[x-1][0] += dx[cur_direction]
            robots[x-1][1] += dy[cur_direction]
            if robots[x-1][0] > A or robots[x-1][1] > B or robots[x-1][0] <= 0 or robots[x-1][1] <= 0:
                print(f'Robot {x} crashes into the wall')
                exit(0)
            for j in range(N):  # 로봇이 서로 부딪치는지 확인
                if j != x-1:
                    if robots[x-1][0] == robots[j][0] and robots[x-1][1] == robots[j][1]:
                        print(f'Robot {x} crashes into robot {j+1}')
                        exit(0)
print("OK")