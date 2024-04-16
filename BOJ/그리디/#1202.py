import sys, heapq

input = sys.stdin.readline

N, K = map(int, input().split())
j = []
for _ in range(N):
    M, V = map(int, input().split())
    j.append([M, V])  # 무게, 가격
bags = [int(input().rstrip()) for _ in range(K)]

j.sort()
bags.sort()
result = 0
tmp = []  # 보석가격 저장
# 용량이 작은 가방부터 채워준다
for bag in bags:
    while j and j[0][0] <= bag:   # 보석리스트가 비어있지 않고 가장 가벼운 보석무게가 b 이하이면
        heapq.heappush(tmp, -j[0][1])  # 가격 저장
        heapq.heappop(j)
    if tmp:
        result -= heapq.heappop(tmp)
print(result)