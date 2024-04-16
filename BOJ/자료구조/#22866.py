import sys
input = sys.stdin.readline

N = int(input())
heights = list(map(int, input().split()))
visible = [[] for _ in range(N)]  # 각 위치에서 보이는 [인덱스, 높이] 저장

# abs를 사용해서 저장

# 왼쪽 방향에서 보이는 건물
stack = []
for i in range(N):
    while stack and stack[-1][1] <= heights[i]:
        stack.pop()
    if stack:
        visible[i].append(stack[-1])
    stack.append((i, heights[i]))

# 오른쪽 방향에서 보이는 건물
stack = []
for i in range(N-1, -1, -1):
    while stack and stack[-1][1] <= heights[i]:
        stack.pop()
    if stack:
        visible[i].append(stack[-1])
    stack.append((i, heights[i]))

for i in range(N):
    if visible[i]:
        # 건물까지의 거리 계산
        distance = [abs(i-building[0]) for building in visible[i]]

    else:  # 보이는 건물이 없는 경우
        print(0)