# 정답
# 높이가 1~10억까지의 정수 중 하나 -> 순차탐색X
n, m = map(int, input().split())  # 떡의 갯수, 요청한 떡의 길이
heights = list(map(int, input().split()))

start = 0
end = max(heights)

result = 0
while (start <= end):
    total = 0

    mid = (start+end) // 2
    for x in heights:
        if x > mid:
            total += (x-mid)  # 손님이 가져가는 떡의 양 total 구하기

    if total < m:  # 떡의 양이 부족한 경우 -> 자르는 높이를 줄여야한다
        end = mid-1
    else:
        result = mid  # 최대한 덜 잘랐을때를 구해야하므로 일단 저장해두기
        start = mid+1

print(result)