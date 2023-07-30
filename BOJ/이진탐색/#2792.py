import sys
input = sys.stdin.readline

N, M = map(int, input().split())
jewlry = []  # 보석 갯수
for _ in range(M):
    jewlry.append(int(input()))

result = 0
start, end = 1, max(jewlry)  # 1개 ~ 보석함 내 최대 보석 갯수

while start <= end:
    mid = (start + end) // 2  # mid = 한사람이 가져가는 보석의 수
    people = 0
    for i in jewlry:
        if i % mid == 0:
            people += i//mid
        else:
            people += i//mid+1  # 나누어 떨어지지 않는다면 1명 더 추가
    if people > N:  # 보석을 더 많이 나눠준다
        start = mid + 1
    else:
        end = mid - 1
        result = mid
print(result)