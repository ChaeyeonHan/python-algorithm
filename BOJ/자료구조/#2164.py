# 스택 -> 시간초과
# import sys
# input = sys.stdin.readline
#
# N = int(input())
# stack = [_ for _ in range(1, N+1)]
#
# while len(stack) != 1:
#     stack.pop(0)
#     x = stack.pop(0)
#     stack.append(x)
# print(stack[0])

import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
q = deque([i for i in range(1, N+1)])

while len(q) != 1:
    q.popleft()
    q.append(q.popleft())

print(q[0])