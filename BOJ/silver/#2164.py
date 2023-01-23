# import sys
# from collections import deque
# N = int(sys.stdin.readline().rstrip())
# deq = deque([i for i in range(1, N+1)])
#
# # print(deq)  # deque([1, 2, 3, 4])
#
# while True:
#     deq.popleft()  # 맨 위의 하나 버리기
#     deq.append(deq.popleft())
#     if len(deq) == 1:
#         break
#
# print(deq[0])

# indexError -> 입력받는 정수 N에 1이 들어가면 while문에서 먼저 popleft되고, 길이가 0인 비어있는 덱이 되어 에러가 발생
# 위의 풀이가 런타임에러가 발생해서 if문 지우고 while len(deq) > 1로 수정

import sys
from collections import deque
N = int(sys.stdin.readline().rstrip())
deq = deque([i for i in range(1, N+1)])


while len(deq) > 1:
    deq.popleft()  # 맨 위의 하나 버리기
    deq.append(deq.popleft())

print(deq[0])
