# 주어진 입력값이 매우 크다
import sys

def binary_search(arr, value, start, end):
    if start > end:  # 값이 없는 경우
        return 0
    mid = (start + end) // 2
    if arr[mid] == value:
        return 1
    elif arr[mid] > value:
        return binary_search(arr, value, start, mid-1)
    else:  # arr[mid] < value
        return binary_search(arr, value, mid+1, end)

n = int(sys.stdin.readline())  # 상근이가 가진 카드갯수
nums_sg = list(map(int, sys.stdin.readline().split()))  # 상근이가 가진 카드
nums_sg.sort()  # 상근이 카드 정렬
m = int(sys.stdin.readline())  # 판단갯수
nums_list = list(map(int, sys.stdin.readline().split()))

for i in range(len(nums_list)):
    result = binary_search(nums_sg, nums_list[i], 0, len(nums_sg) - 1)
    print(result, end=" ")