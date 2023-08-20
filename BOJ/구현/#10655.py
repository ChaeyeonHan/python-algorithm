import sys
# import math
input = sys.stdin.readline

N = int(input())
graph = []
for _ in range(N):
    a, b = map(int, input().split())
    graph.append((a, b))

distance = []
for i in range(1, N):
    cur_distance = abs(graph[i-1][0]-graph[i][0]) + abs(graph[i-1][1]-graph[i][1])
    distance.append(cur_distance)

total = sum(distance)
min_distance = 1e9  # math.inf
for i in range(1, N-1):  # 1번과 N번 체크포인트를 빼고 건너뛰는 모든 경우
    cur = total - (distance[i-1]+distance[i]) + abs(graph[i+1][0]-graph[i-1][0]) + abs(graph[i+1][1]-graph[i-1][1])
    min_distance = min(cur, min_distance)
print(min_distance)