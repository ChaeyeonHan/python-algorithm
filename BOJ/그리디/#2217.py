import sys
input = sys.stdin.readline

N = int(input())
rope = []
for _ in range(N):
    rope.append(int(input()))
rope.sort()

weight = 0
for i in range(N):
    if weight < rope[i]*(N-i):
        weight = rope[i]*(N-i)
print(weight)