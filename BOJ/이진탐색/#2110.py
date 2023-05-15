import sys
input = sys.stdin.readline

N, C = map(int, input().split())
position = [int(input()) for _ in range(N)]
position.sort()
# 가장 인접한 공유기 사이의 최대 거리 구하기
# 집 사이의 최소/최대 거리
start, end = 1, position[-1] - position[0]
result = 0

while start <= end:
    mid = (start + end) // 2
    cnt = 1  # 설치하는 공유기 갯수
    current = position[0]  # 마지막으로 설치된 공유기의 위치

    for i in range(1, N):
        if current + mid <= position[i]:  # 현재 집에서 다음 집까지의 거리가 mid 이상인 경우 -> 공유기 설치
            cnt += 1
            current = position[i]
    if cnt >= C:  # 지정한 갯수보다 현재 설치된 공유기 갯수가 많다면 -> 설치 간격을 넓힌다
        result = mid
        start = mid + 1
    else:  # 지정한 갯수보다 현재 설치된 공유기 갯수가 적다면 -> 설치 간격을 좁힌다
        end = mid - 1

print(result)