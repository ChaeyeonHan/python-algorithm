import sys
input = sys.stdin.readline

N = int(input())
stack = []
answer = 0

for _ in range(N):
    x, y = map(int, input().split())
    while len(stack) > 0 and stack[-1] > y:
        stack.pop()
        answer += 1
    if len(stack) > 0 and stack[-1] == y:
        continue
    stack.append(y)

while len(stack) > 0:
    if stack[-1] > 0:
        answer += 1
    stack.pop()

print(answer)
