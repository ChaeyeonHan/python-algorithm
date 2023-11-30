import heapq

def solution(scoville, K):
    heap = []
    cnt = 0
    for i in range(len(scoville)):  # heapq.heapify(scoville)
        heapq.heappush(heap, scoville[i])

    while heap[0] < K:
        a = heapq.heappop(heap)
        b = heapq.heappop(heap)
        heapq.heappush(heap, a + b * 2)
        cnt += 1
        if len(heap) == 1 and heap[0] < K:
            return -1
    return cnt


print(solution([1, 2, 3, 9, 10, 12], 7))