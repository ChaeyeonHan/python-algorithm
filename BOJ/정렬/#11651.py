import sys
input = sys.stdin.readline

N = int(input())
position = []
for _ in range(N):
    a, b = map(int, input().split())
    position.append((a, b))
position.sort(key=lambda x: (x[1], x[0]))

for i in range(N):
    print(position[i][0], position[i][1])