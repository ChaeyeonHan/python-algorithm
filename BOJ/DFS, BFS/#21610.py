import sys
input = sys.stdin.readline

N, M = map(int, input().split())
bucket = [list(map(int, input().split())) for _ in range(N)]  # 물의 양 저장

# ←, ↖, ↑, ↗, →, ↘, ↓, ↙
dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]


# 구름 이동함수
def move_cloud(d, s):
    next_cloud = []
    for i in range(len(cloud)): 
        x, y = cloud[i][0], cloud[i][1]
        x = (x+dx[d-1]*s)%N
        y = (y+dy[d-1]*s)%N
        next_cloud.append((x, y))
        pre_cloud[x][y] = True
        bucket[x][y] += 1
    return next_cloud
        

# 물 복사 마법
def water_magic():
    for k in cur_cloud:
        cnt = 0
        x, y = k[0], k[1]
        for i in range(1, 8, 2):  # 대각선 방향 확인
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if bucket[nx][ny] != 0:
                    cnt += 1
        bucket[x][y] += cnt 
    
# 구름 생성 함수
def make_cloud():
    next_cloud = []
    
    for i in range(N):
        for j in range(N):
            if bucket[i][j] >= 2:
                if not pre_cloud[i][j]:
                    bucket[i][j] -= 2
                    next_cloud.append((i, j))
    return next_cloud
                    

cloud = [(N-1, 0), (N-1, 1), (N-2, 0), (N-2, 1)]  # 구름 위치 저장
for _ in range(M):
    d, s = map(int, input().split())
    pre_cloud = [[0]*N for _ in range(N)]
    
    cur_cloud = move_cloud(d ,s)
    water_magic()
    cloud = make_cloud()

print(sum(sum(row) for row in bucket))