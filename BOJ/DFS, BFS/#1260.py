def dfs(V):
    visited[V] = 1  # 방문한 곳은 1로 바꾸기
    print(V, end=' ')
    for i in range(1, N+1):
        if (visited[i] == 0 and matrix[V][i] == 1):  # 방문 안했고 인접한 곳 찾아 dfs실행
            dfs(i)

def bfs(V):
    queue = [V]  # 방문할 곳을 순서대로 큐에 넣는다
    visited[V] = 0  # dfs를 완료해서 visited배열을 0으로 방문처리
    while queue:  # 큐 안에 데이터가 없을때까지
        V = queue.pop(0)
        print(V, end=' ')
        for i in range(1, N+1):
            if(visited[i] == 1 and matrix[V][i] == 1):
                queue.append(i)
                visited[i] = 0

N, M, V = map(int, input().split())

matrix = [[0] * (N+1) for i in range(N+1)]

visited = [0]*(N+1)  # 방문한곳 체크하기 위한 배열

for i in range(M):  # 연결된 노드 1로 표시해주기
    a, b = map(int, input().split())
    matrix[a][b] = matrix[b][a] = 1

dfs(V)
print()
bfs(V)


