# 1. 시간초과 -> 시간복잡도 : O(N*K)
# import sys
# input = sys.stdin.readline
#
# N, d, k, c = map(int, input().split())
# sushi = []
# for _ in range(N):
#     sushi.append(int(input()))
#
# # 구간 인덱스(연속적으로 k개의 초밥 선택)
# left, right = 0, k
#
# answer = 0
# while left < N:
#     nums = set()
#     for i in range(left, right):
#         i %= N
#         nums.add(sushi[i])
#
#     nums.add(c)  # 쿠폰 추가
#     answer = max(answer, len(nums))
#
#     # 한칸씩 밀어주기
#     left += 1
#     right += 1
#
# print(answer)

# 2. 슬라이딩 윈도우(딕셔너리 이용)
import sys
input = sys.stdin.readline
N, d, k, c = map(int, input().split())
sushi = []

for _ in range(N):
    sushi.append(int(input()))

left, right = 0, 0
dict = {}
result = 0

while right < k:
    if sushi[right] not in dict.keys():
        dict[sushi[right]] = 1
    else:
        dict[sushi[right]] += 1
    right += 1

if c not in dict.keys():
    dict[c] = 1
else:
    dict[c] += 1

# 슬라이딩 윈도우
while left < N:
    result = max(result, len(dict))
    # 가장 왼쪽 초밥 제거
    dict[sushi[left]] -= 1
    if dict[sushi[left]] == 0:  # 0이면 dict에서 삭제
        del dict[sushi[left]]
    if sushi[right % N] not in dict.keys():
        dict[sushi[right%N]] = 1
    else:
        dict[sushi[right%N]] += 1
    # 한칸씩 밀어주기
    left += 1
    right += 1

print(result)

# 3. defaultdict 이용
import sys
from collections import defaultdict

input = sys.stdin.readline
N, d, k, c = map(int, input().split())
sushi = []

for _ in range(N):
    sushi.append(int(input()))

left, right = 0, 0
dict = defaultdict(int)
result = 0

while right < k:
    dict[sushi[right]] += 1
    right += 1

dict[c] += 1  # 쿠폰

while left < N:
    result = max(result, len(dict))
    # 맨 왼쪽 초밥 제거
    dict[sushi[left]] -= 1
    if dict[sushi[left]] == 0:
        del dict[sushi[left]]
    dict[sushi[right%N]] += 1
    left += 1
    right += 1

print(result)