# heap자료구조 이용 -> 특정 노드까지 최단거리 정보를 힙에 담아서 처리하기에, 빠르게 찾을 수 있음
# get_smallest_node()함수를 사용하지 않고 우선순위 큐를 이용하는 방식으로 대체
import sys
import heapq

int = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
start = int(input())
graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)
# 방문처리 확인하는 테이블 필요X

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)  # 최단 거리가 가장 짧은 노드에 대한 정보 꺼내기
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[j[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))  # (거리, 노드)


dijkstra(start)

for i in range(1, n + 1):
    if distance[i] == INF:
        print(-1)
    else:
        print(distance[i])
