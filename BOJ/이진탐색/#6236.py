import sys
input = sys.stdin.readline

N, M = map(int, input().split())
money = [int(input()) for _ in range(N)]
start, end = min(money), sum(money)
result = 0

while start <= end:
    mid = (start + end) // 2
    cnt = 1  # 인출횟수 카운트
    now = mid  # 현재 가진 돈

    for i in range(N):
        if now < money[i]:  # 돈이 부족하면 인출
            cnt += 1
            now = mid
        now -= money[i]
    if cnt > M or mid < max(money):  # 주어진 횟수보다 많이 인출하거나 mid가 예산 최댓값보다 작으면  -> 인출 금액을 늘린다
        start = mid + 1

    else:  # 주어진 횟수보다 인출을 적게함 -> 인출 금액을 줄인다
        end = mid - 1
        result = mid

print(result)