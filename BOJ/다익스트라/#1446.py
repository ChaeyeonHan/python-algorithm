import sys
import heapq
input = sys.stdin.readline

INF = int(1e9)

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

N, D = map(int, input().split())  #  지름길 갯수, 고속도로 길이. D까지 가야한다
graph =[[] for _ in range(D+1)]
distance = [INF] * (D+1)
distance[0] = 0

for i in range(D):  # 거리를 모두 1로 초기화
    graph[i].append((i+1, 1))

for _ in range(N):  # 지름길이 있는 경우 업데이트
    start, end, length = map(int, input().split())
    if end > D:
        continue
    graph[start].append((end, length))

dijkstra(0)
print(distance[D])

