import sys
input = sys.stdin.readline

N = int(input())
colors = list(input().rstrip())
# print(colors)
B, R = 0, 0
for i in range(len(colors)):
    if colors[i] == 'B':
        B += 1
    else:
        R += 1
print(B, R)