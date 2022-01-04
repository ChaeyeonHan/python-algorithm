#  파라매트릭 서치(parametric search) : 최적화문제를 결정 문제로 바꾸어 해결
#  떡 높이를 이진탐색해서 구하기
N, M = map(int, input().split())
array = list(map(int, input().split()))

start = 0
end = max(array)  # 최댓값으로 설정

result = 0
while (start <= end):
    mid = (start+end)//2
    total = 0
    for i in array:
        if i > mid:
            total += i-mid
    if total < M:
        end = mid - 1
    else:
        result = mid  # 최대한 덜 잘랐을 때 구하기.
        start = mid + 1

print(result)
