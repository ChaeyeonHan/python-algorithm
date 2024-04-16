# 용액의 특성값 주어지면 두개 더해서 0에 가까운 값 만드는거 찾기

import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))

nums.sort()

# 인덱스값으로
start, end = 0, N-1
minAbs = sys.maxsize
while start < end:
    twoSum = nums[start] + nums[end]
    if abs(twoSum) < minAbs:  # 절댓값이 더 작으면
        minAbs = abs(twoSum)
        result = [nums[start], nums[end]]
        if abs(twoSum) == 0:
            break
    if twoSum < 0:
        start += 1
    else:
        end -= 1  
print(result[0], result[1])