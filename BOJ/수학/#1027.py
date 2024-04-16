import sys
import math
input = sys.stdin.readline

# 기준이 되는 K번째 빌딩에서, 왼쪽으로 갈수록 기울기가 작아지고 오른쪽으로 갈수록 기울기가 커져야 한다
N = int(input())
heights = list(map(int, input().split()))
result = 0

for k in range(N):
    left_slope = math.inf
    right_slope = -math.inf
    cnt = 0
    for i in range(k-1, -1, -1):  # 왼쪽 탐색
        temp = (heights[i]-heights[k]) / (i-k)
        if temp < left_slope:
            left_slope = temp
            cnt += 1
    for i in range(k+1, N):  # 오른쪽 탐색
        temp = (heights[i]-heights[k]) / (i-k)
        if temp > right_slope:
            right_slope = temp
            cnt += 1
    result = max(cnt, result)
print(result)