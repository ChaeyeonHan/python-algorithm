import sys
input = sys.stdin.readline

# 1. 투 포인터
# 리스트 양 끝에 포인터를 위치시키고, 합이 음수라면 왼쪽 포인터를 한칸씩 오른쪽으로 이동
# 합이 양수라면 오른쪽 포인터를 한칸씩 왼쪽으로 이동시켜 절댓값이 작아지도록 한다.(두 포인터가 만나기 전까지 시행)
N = int(input())
nums = list(map(int, input().split()))
left, right = 0, N-1  # 시작 포인터 위치
nums_left, nums_right = 0, 0

answer = sys.maxsize
while left < right:
    temp = nums[left] + nums[right]
    if abs(temp) < answer:
        nums_left = nums[left]
        nums_right = nums[right]
        answer = abs(temp)
    if temp == 0:
        break
    elif temp < 0:
        left += 1
    elif temp > 0:
        right -= 1

print(nums_left, nums_right)


# 2. 이진탐색
N = int(input())
nums = list(map(int, input().split()))

answer = sys.maxsize
left, right = 0, N-1
nums_left, nums_right = 0, 0

for i in range(N-1):
    current = nums[i]
    # i번째의 값과 i+1 ~ n-1까지의 합을 구해서 0가 가까운 쌍을 찾는다
    start = i+1
    end = N-1
    while start <= end:
        mid = (start + end) // 2
        temp = current + nums[mid]

        if abs(temp) < answer:
            answer = abs(temp)
            nums_left = i
            nums_right = mid

        if temp == 0:
            break
        elif temp < 0:
            start = mid + 1
        elif temp > 0:
            end = mid - 1

print(nums[nums_left], nums[nums_right])