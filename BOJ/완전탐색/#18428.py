import sys
input = sys.stdin.readline

N = int(input())
graph = []

for _ in range(N):
    graph.append(input().split())
print(graph)