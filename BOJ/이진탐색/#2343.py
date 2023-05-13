import sys
input = sys.stdin.readline

N, M = map(int, input().split())
data = list(map(int, input().split()))

start, end = max(data), sum(data)

while start <= end:
    mid = (start + end) // 2  # 블루레이의 크기
    div, temp = 1, 0  # cnt는 블루레이 갯수, temp는 블루레이 길이를 갱신하기 위한 변수
    for i in range(N):
        if temp + data[i] <= mid:  # 블루레이에 다음 강의를 더 넣을 수 있다면
            temp += data[i]
        else:
            temp = data[i]
            div += 1
    if div <= M:  # 갯수가 부족하다면, mid의 크기를 줄인다
        answer = mid
        end = mid - 1
    else:  # 갯수가 많다면, mid의 크기를 늘린다
        start = mid + 1
print(answer)
