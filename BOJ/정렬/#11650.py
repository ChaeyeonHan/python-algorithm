import sys
input = sys.stdin.readline

N = int(input())
position = []
for _ in range(N):
    position.append(list(map(int, input().split())))

# print(position)
position.sort(key=lambda x: (x[0], x[1]))
for i in range(N):
    print(position[i][0], position[i][1])