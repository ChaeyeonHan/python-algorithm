# 내가 풀다 놓친 부분
# 1. (상근이가 가진 숫자 갯수 > 주어진 숫자 갯수 일때), 이진탐색을 주어진 숫자 갯수만큼 실행하기에
# 값이 존재하는지는 찾아주지만, 여러개 존재한다면 몇개인지는 찾지 못한다.

# 2.
# 입력예시 : 10 // 6 3 2 10 10 10 -10 -10 7 3 // 8 // 10 10 -5 2 3 4 5 -10 가 들어왔을떄
# 3 3 0 1 2 0 0 2 가 나와야한다
# 내가 푼건 상근이 숫자 리스트에서 값을 삭제해서 리스트 크기가 한개씩 작아지고있음. 이러면X
# import sys
# def binary_search(arr, value, start, end, count):
#     if start > end:
#         return count
#     mid = (start + end) // 2
#     if arr[mid] == value:
#         count += 1
#         print(str(value) + " 찾았음")
#         # print(count)
#         del arr[mid]
#         return binary_search(arr, value, start, len(arr)-1, count)
#     elif arr[mid] > value:
#         return binary_search(arr, value, start, mid-1, count)
#     else:
#         return binary_search(arr, value, mid+1, end, count)
#
# n = int(sys.stdin.readline())
# nums_sg = list(map(int, sys.stdin.readline().split()))
# nums_sg.sort()  # 상근이 카드 정렬
#
# m = int(sys.stdin.readline())
# nums_list = list(map(int, sys.stdin.readline().split()))
# result_nums = [0]*len(nums_list)  # 숫자 몇개 있는지 세는 리스트
#
# # 리스트에 숫자 몇개있는지 세줘야하기에
# # 존재하는지 찾으면, mid값 찾아오면 리스트에서 mid자리에 있는 값을 삭제하고 1개 ++해줌.
#
# for i in range(len(nums_list)):
#     count = 0
#     a = binary_search(nums_sg, nums_list[i], 0, len(nums_sg)-1, count)  # count값 리턴
#     print(str(i) + "번째")
#     print(nums_sg)
#     print(nums_list)
#     # print(a)
#     result_nums[i] = a
#
# print(result_nums)

# 딕셔너리 이용
# 숫자를 dict의 key로, 카드 숫자를 value로 해서 사전을 만든다
n = int(input())
cards = list(map(int, input().split()))
cards.sort()  # 상근이 카드

m = int(input())
targets = list(map(int, input().split()))

# 딕셔너리에 담아주기
dic = dict()
for i in cards:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

for i in targets:
    if i in dic:
        print(dic[i], end=' ')
    else:
        print(0, end=' ')