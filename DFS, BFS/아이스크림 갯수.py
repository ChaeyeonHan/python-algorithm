# DFS사용 (스택이용)

N, M = map(int, input().split())

# graph라는 2차원 리스트를 사용해 맵의 정보 저장하기
graph = []
for i in range(N):
    graph.append(list(map(int, input())))
'''
print(graph)  2X3 , 123 456 (입력시 띄어쓰기없이)
[[1,2,3], [4,5,6]]
'''

def dfs(x, y):
    # 범위를 벗어난 경우 종료시킨다
    if x <= -1 or x >= N or y <= -1 or y >= M:
        return False
    if graph[x][y] == 0:  # 방문하지 않은 경우
        graph[x][y] == 1  # 방문처리
        dfs(x-1, y)
        dfs(x,y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False

result = 0
for i in range(N):
    for j in range(M):
        if dfs(i,j) == True:
            result += 1

print(result)

