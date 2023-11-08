import sys
input = sys.stdin.readline

# 현재 건물 기준으로 양쪽 각각 2 건물씩 확인해서 count
# 5개의 건물을 확인했을때, 현재 건물의 height이 가장 높아야 됨
T = 1
while T < 11:
    N = int(input())  # 건물의 갯수
    heights = list(map(int, input().split()))  # 왼쪽 2개, 오른쪽 2개는 항상 높이 0
    cnt = 0
    for i in range(2, N-2):  # 2부터 N-2까지
        cur = heights[i]  # 현재 건물 높이
        max_height = max(heights[i-2], heights[i-1], heights[i+1], heights[i+2])
        if heights[i] - max_height>0:
            cnt += heights[i] - max_height

    print("#{} {}".format(T, cnt))
    T += 1