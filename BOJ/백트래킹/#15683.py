# cctv 방향을 결정해서 사각지대의 최소 크기를 구한다
# 각 숫자마다 방향이 다른데 어떻게 표시할건지?코드로
# 0은 빈칸, 1~5는 cctv, 6은 벽

import sys
import copy

# 상하좌우
dx = [-1, 1, 0, 0] 
dy = [0, 0, 1, -1]

N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

# cctv번호별 탐색 가능한 방향 설정
# dx, dy에 넣은 상하좌우 순서대로
cctv_direction = [
    [],
    [[0], [1], [2], [3]],  # 1번
    [[0, 1], [2, 3]],  # 2번
    [[0, 2], [0, 3], [1, 2], [1, 3]],  # 3번
    [[1, 2, 3], [0, 2, 3], [0, 1, 3], [0, 1, 2]],  # 4번
    [[0, 1, 2, 3]]  # 5번
]

def dfs(matrix, depth):
    global answer
    if depth == len(cctv_pos):  # 모든 cctv 탐색하면 종료
        count = 0
        for i in range(N):  # 사각지대 구하기
            count += matrix[i].count(0)
        answer = min(answer, count)
        return
    else:
        # 그래프를 복제
        matrix_copy = copy.deepcopy(matrix)
        x, y, cctv_type = cctv_pos[depth]  # 탐색할 cctv
        for cctv_dir in cctv_direction[cctv_type]:  # cctv종류별로 움직일 수 있는 방향 모두 탐색
            # 감시영역 구하기
            watch(x, y, cctv_dir, matrix_copy)
            dfs(matrix_copy, depth+1)
            matrix_copy = copy.deepcopy(matrix)  # 전단계로 이동

# 감시함수
def watch(x, y, direction, matrix):
    for d in direction:
        nx, ny = x, y
        while True:
            nx += dx[d]
            ny += dy[d]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:  # 범위 넘어가면 중단
                break
            if matrix[nx][ny] == 6:  # 벽이면 중단
                break
            elif matrix[nx][ny] == 0:
                matrix[nx][ny] = '#'

# 2차원 배열 돌면서 cctv만나면 check함수 실행
# 0을 가장 많이 append 할 수 있는 방향으로 선택
cctv_pos = []  # cctv 위치,타입 저장
for i in range(N):
    for j in range(M):
        if 1 <= matrix[i][j] <= 5:
            cctv_pos.append((i, j, matrix[i][j]))

answer = int(1e9)
dfs(matrix, 0)
print(answer)