import sys, heapq
input = sys.stdin.readline

N = int(input())
cards = []
for _ in range(N):
    num = int(input())
    heapq.heappush(cards, num)

result = 0
while len(cards) > 1:
    a = heapq.heappop(cards)
    b = heapq.heappop(cards)
    result += (a+b)
    heapq.heappush(cards, a+b)

print(result)