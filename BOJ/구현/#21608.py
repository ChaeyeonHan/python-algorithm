import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

N = int(input())
stu_len = N*N
pos = [[0 for _ in range(N)] for _ in range(N)]

# [학생번호, 좋아하는 친구들 번호]
students = []
for _ in range(stu_len):
    students.append(list(map(int, input().split())))

for student in students:
    number = student[0]  # 현재 앉힐 학생
    able_position = []  # 앉을 수 있는 자리를 넣을 리스트
    for i in range(N):
        for j in range(N):
            if pos[i][j] == 0:  # 현재 자리가 비어있다면
                like = 0  # 선호 학생 수
                blank = 0  # 자리 주위의 빈자리 갯수
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if nx < 0 or ny < 0 or nx >= N or ny >= N:
                        continue
                    if pos[nx][ny] in students[1:]:  # 해당 위치에 선호하는 학생이 있다면
                        like += 1
                    if pos[nx][ny] == 0:  # 아직 빈 자리라면
                        blank += 1
                able_position.append([like, blank, i, j])
    able_position.sort(key=lambda x: (-x[0], -x[1], x[2], x[3]))  # 앉힐 자리를 like, blank는 내림차순, 좌표는 오름차순 정렬
    pos[able_position[0][2]][able_position[0][3]] = number

happy = 0
students.sort()

for i in range(N):
    for j in range(N):
        like_cnt = 0
        num = pos[i][j]
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]
            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue
            if pos[nx][ny] in students[num - 1][1:]:  # 선호하는 학생이라면
                like_cnt += 1
        if like_cnt != 0:
            happy += (10 ** (like_cnt - 1))

print(happy)