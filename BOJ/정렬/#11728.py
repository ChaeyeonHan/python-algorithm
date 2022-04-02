# import sys
# input = sys.stdin.readline().strip()

N, M = map(int, input().split())
nums1=[]
nums2=[]

nums1 = list(map(int, input().split()))
nums2 = list(map(int, input().split()))
#
# result=[]
#
# while nums1 and nums2:
#     if nums1[0] >= nums2[0]:
#         result.append(nums2.pop(0))
#     else:
#         result.append(nums1.pop(0))
# result = result + nums1 + nums2  # 맨 마지막 하나 남은 수 더해주기
answer = nums1 + nums2
answer.sort()

for num in answer:
    print(num, end=' ')