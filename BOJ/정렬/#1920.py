# 풀이1 : 탐색시간을 줄이기 위해 set이용
import sys
input = sys.stdin.readline

N = int(input())
nums = set(list(map(int, input().split())))
M = int(input())
M_lists = list(map(int, input().split()))

for i in M_lists:
    print(1) if i in nums else print(0)

for i in M_lists:
    if i in nums:
        print(1)
    else:
        print(0)

# 풀이2 : 이분탐색
import sys

input = sys.stdin.readline

N = int(input())
nums = list((map(int, input().split())))
nums.sort()  # 정렬
M = int(input())
M_list = list(map(int, input().split()))


def binary_search(target):
    start = 0
    end = N - 1
    while start <= end:
        mid = (start + end) // 2
        if nums[mid] == target:
            return True
        elif nums[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return False


for i in range(len(M_list)):
    if binary_search(M_list[i]):
        print(1)
    else:
        print(0)