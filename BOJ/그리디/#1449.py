import sys
input = sys.stdin.readline

N, L = map(int, input().split())
array = list(map(int, input().split()))
array.sort()

start = array[0]  # 테이프 붙이는 시작 지점
cnt = 1

for spot in array[1:]:
    if (spot+0.5) - (start-0.5) <= L:
        continue  # 기존 테이프 사용
    else:
        start = spot
        cnt += 1

print(cnt)