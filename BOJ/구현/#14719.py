import sys
input = sys.stdin.readline

H, W = map(int, input().split())
blocks = list(map(int, input().split()))
result = 0

for i in range(1, W-1):
    left = max(blocks[:i])
    right = max(blocks[i+1:])

    min_height = min(left, right)
    if blocks[i] < min_height:
        result += (min_height - blocks[i])
print(result)