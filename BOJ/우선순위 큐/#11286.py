import sys
import heapq

heap = []
N = int(sys.stdin.readline())

for _ in range(N):
    num = int(sys.stdin.readline())
    if num == 0:
        if len(heap):  # 절댓값이 가장 작은거 빼기
            print(heapq.heappop(heap)[1])
        else:  # 길이가 0이면
            print(0)
    else:
        heapq.heappush(heap, (abs(num), num))  # (절댓값, 원래값)의 튜플로 넣어준다(맨 앞 숫자만으로 정렬함)