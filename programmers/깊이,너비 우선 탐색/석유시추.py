from collections import deque
from collections import defaultdict

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# land 값을 석유가 있음을 뜻하는 1에서 석유의 id로 바꿔준다

def bfs(i, j, N, M, oil, land):
    amount = 1  # 처음 시작부터 count
    land[i][j] = oil  # 덩어리 구분 변수 지정
    queue = deque()
    queue.append((i, j))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and land[nx][ny] == 1:
                amount += 1
                land[nx][ny] = oil
                queue.append((nx, ny))
    return amount


def solution(land):
    answer, oil = 0, 2
    N = len(land)
    M = len(land[0])

    # defaultdict 생성
    amount_of = defaultdict(int)

    for i in range(N):
        for j in range(M):
            if land[i][j] == 1:
                amount_of[oil] = bfs(i, j, N, M, oil, land)  # 해당 석유 덩어리에 석유가 얼만큼 있는지 계산
                oil += 1  # (oil갯수 - 2) 만큼 석유 덩어리 존재

    # 모든 열을 순회하면서 구멍을 뚫으며
    for j in range(M):
        oil_types = set(land[i][j] for i in range(N))  # 몇번째 석유 덩어리랑 만나는지 set으로 구하기
        amount = 0
        for oil in oil_types:
            amount += amount_of[oil]
        answer = max(answer, amount)
    return answer