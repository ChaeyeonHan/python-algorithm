import sys
from collections import deque

T = int(sys.stdin.readline())
while T:
    order = []  # 인쇄 순서 저장
    N, M = map(int, sys.stdin.readline().split())

    deq = deque(list(map(int, sys.stdin.readline().split())))  # 중요도 입력받기
    for i in range(len(deq)):
        deq[i] = [deq[i], i]  # 현재 문서의 위치도 함께 저장
    # print(deq)  # deque([[1, 0], [2, 1], [3, 2], [4, 3]])
    while len(deq):  # 문서가 다 인쇄될때까지
        if max(deq)[0] > deq[0][0]:
            deq.append(deq.popleft())
        else:
            order.append(deq.popleft())

    for i in range(N):
        if order[i][1] == M:
            print(i+1)
            break
    T = T-1