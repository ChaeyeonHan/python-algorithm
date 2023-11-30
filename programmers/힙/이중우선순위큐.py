import sys, heapq
input = sys.stdin.readline

def solution(operations):
    min_heap = []  # 최소힙
    max_heap = []  # 최대힙
    for i in range(len(operations)):
        op, num = operations[i].split()
        # print(op, num)
        num = int(num)

        if op == 'I':  # 숫자 삽입
            heapq.heappush(min_heap, num)
            heapq.heappush(max_heap, -num)
        else:
            if len(min_heap) == 0:
                continue
            elif num == -1:  # 최솟값 삭제
                min_value = heapq.heappop(min_heap)
                max_heap.remove(-min_value)
            elif num == 1:  # 최댓값 삭제
                max_value = heapq.heappop(max_heap)
                min_heap.remove(-max_value)

    if len(min_heap) == 0:
        return [0, 0]
    else:
        return [-heapq.heappop(max_heap), heapq.heappop(min_heap)]

print(solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]))
print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]))