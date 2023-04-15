# 시간 복잡도 O(V^) : V는 노드의 갯수
import sys
input = sys.stdin.readline
INF = int(1e9)  # 무한을 의미

n, m = map(int, input().split())  # 노드와 간선의 갯수 입력
start = int(input())  # 시작노드 입력

graph = [[] for _ in range(n+1)]  # 각 노드에 연결된 정보를 나타내는 리스트
visited = [False] * (n+1)  # 방문여부 체크
distance = [INF] * (n+1)  # 최단 거리 테이블 모두 무한으로 초기화

# 연결된 노드, 간선에 대한 정보 입력받기
for _ in range(m):  # 간선 m개
    a, b, c = map(int, input().split())  # a노드에서 b노드로 이동하는 비용이 c
    graph[a].append((b, c))


def get_smallest_node():  # 방문하지 않은 노드 중에 최단거리가 가장 짧은 노드번호 찾아 반환하는 함수
    min_value = INF
    index = 0
    for i in range(1, n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

def dijkstra(start):
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1]

    for i in range(n-1):
        now = get_smallest_node()  # 현재 최단 거리가 가장 짧은 노드 찾아오기
        visited[now] = True
        for j in graph[now]:  # now노드와 연결된 다른 노드 확인
            cost = distance[now] + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost
dijkstra(start)

for i in range(1, n+1):  # start노드에서 시작해서 모든 노드로 가는 최단거리 출력
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])