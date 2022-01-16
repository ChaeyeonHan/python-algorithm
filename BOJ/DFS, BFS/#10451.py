import sys
sys.setrecursionlimit(10 ** 6)
# 파이썬에서는 재귀 최대 깊이의 기본 설정이 1000회이기에, 아래처럼 최대 깊이를 늘려준다.

def dfs(v):
    visited[v] = 1  # 현재 노드 방문표시
    pos = arr[v]  # 연결된 곳으로 이동
    if visited[pos] == 0:  # 연결된 곳 방문 안했다면
        dfs(pos)


T = int(sys.stdin.readline())  # 테스트 케이스 갯수

for i in range(T):
    N = int(input())
    visited = [0]*(N+1)  # 방문 여부 체크를 위한 리스트
    result = 0
    arr = [0] + list(map(int, sys.stdin.readline().split()))  # 각 노드 연결된 정보 저장을 위한 리스트
    for j in range(1, N+1):
        if visited[j] == 0:
            dfs(j)
            result += 1
    print(result)




