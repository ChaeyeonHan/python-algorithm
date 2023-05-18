import sys
input = sys.stdin.readline

heights = [int(input()) for _ in range(9)]
total = 0

# for i in range(8):
#     for j in range(i+1, 9):
flag = False
for i in range(0, len(heights)-1):
    if flag == True:
        break
    for j in range(i + 1, len(heights)):
        total = sum(heights) - (heights[i] + heights[j])
        if total == 100:
            a, b = heights[i], heights[j]
            heights.remove(a)  # 삭제하려는 값 입력
            heights.remove(b)
            flag = True
            break

heights.sort()
for i in heights:
    print(i)

# combinations 이용
import sys
input = sys.stdin.readline
from itertools import combinations

heights = [int(input()) for _ in range(9)]

seven = list(combinations(heights, 7))

for i in seven:
    if sum(i) == 100:
        for j in sorted(i):
            print(j)
        break