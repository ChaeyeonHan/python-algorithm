# sort() -> 시간초과
# import sys
# input = sys.stdin.readline
#
# N = int(input())
# nums = []
#
# def get_middle(nums):
#     n = len(nums)
#     if n % 2 == 0:  # 짝수개
#         k = n//2-1
#         print(nums[k])
#     else:
#         print(nums[n//2])
#
# for _ in range(N):
#     nums.append(int(input()))
#     nums.sort()
#     get_middle(nums)

import sys
import heapq
input = sys.stdin.readline

N = int(input())
leftHeap = []
rightHeap = []
answer = []

for i in range(N):
    num = int(input())
    if len(leftHeap) == len(rightHeap):
        heapq.heappush(leftHeap, (-num, num))
    else:
        heapq.heappush(rightHeap, (num, num))
    if rightHeap and leftHeap[0][1] > rightHeap[0][0]:
        min = heapq.heappop(rightHeap)[0]
        max = heapq.heappop(leftHeap)[1]
        heapq.heappush(rightHeap, (max, max))
        heapq.heappush(leftHeap, (-min, min))

    answer.append(leftHeap[0][1])

for i in answer:
    print(i)