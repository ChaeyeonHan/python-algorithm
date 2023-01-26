# # 이 풀이는 시간초과가 뜬다...
# import sys
#
# input = sys.stdin.readline
# N = int(input())
# result = 0
# arr = []
#
# for i in range(N):
#     arr.append([int(input()), i+1])  # 인덱스랑 -득표수 같이 저장
#
# arr.sort(key=lambda x: -x[0])
# # print(arr)
# while True:
#     if (arr[0][1] == 1) and (arr[0][0] > arr[1][0]):
#         break
#     arr[0][0] -= 1  # 주민 하나 뺏어와서
#     for i in range(len(arr)):
#         if arr[i][1] == 1:
#             arr[i][0] += 1
#             result += 1
#     arr.sort(key=lambda x: -x[0])
#
# print(result)


# 올바른 풀이(다솜이 혼자 나온 경우까지 고려한!!)
import sys
input = sys.stdin.readline

N = int(input())
votes = [int(input()) for _ in range(N)]
count = 0

cand = votes[1:len(votes)]
dasom = votes[0]

if N == 1:   # 다솜이 혼자 나온 경우
    print(0)
else:
    cand = sorted(cand, reverse=True)  # 투표수 내림차순 정렬
    while cand[0] >= dasom:
        dasom += 1
        cand[0] -= 1
        count += 1  # 주민 한명 데려오기
        cand = sorted(cand, reverse=True)
    print(count)


# 힙을 사용하는 방법
# N != 1 일때, 다솜이의 득표수가 가장 많은 경우를 생각하지 못했는데(ex. input: 2 5 1)
# 다솜이 표까지 포함해서 힙에 넣어주면 복잡해지기에, 다솜이 표를 제외하고 나머지 사람들의 표에대해서만 heap에 넣어준다
import heapq
import sys

input = sys.stdin.readline
heap = []

N = int(input())
count = 0
dasom = 0
for i in range(N):
    votes = int(input())
    if i == 0:  # 다솜이 표
        dasom = votes
    else:
        heapq.heappush(heap, -votes)  # 최대 힙 구현

while True:
    if N == 1:
        print(0)
        break
    votes = -heapq.heappop(heap)
    if votes >= dasom:
        dasom += 1
        count += 1
        heapq.heappush(heap, -(votes-1))
    else:
        break
if N != 1:
    print(count)