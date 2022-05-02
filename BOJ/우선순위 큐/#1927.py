import sys
import heapq

min_heap = []
N = int(sys.stdin.readline())

for i in range(N):
    num = int(sys.stdin.readline())
    if num == 0:  # 최소값 꺼내오기 -> 없으면 0출력
        if len(min_heap):
            print(heapq.heappop(min_heap))
        else:
            print(0)
    else: # 값 넣어주기
        heapq.heappush(min_heap, num)
