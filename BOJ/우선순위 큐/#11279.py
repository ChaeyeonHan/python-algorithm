import sys
import heapq

N = int(sys.stdin.readline())
max_heap = []

for i in range(N):
    num = int(sys.stdin.readline())
    if num == 0:
        if len(max_heap):
            print(-heapq.heappop(max_heap))
        else:
            print(0)
    else:
        heapq.heappush(max_heap, -num)  # 삽입