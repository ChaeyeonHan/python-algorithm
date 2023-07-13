def solution(n, computers):
    answer = 0
    # DFS/BFS 모두 풀이 가능해보임
    visited = [0 for _ in range(n)]

    for i in range(n):
        if visited[i] == 0:
            dfs(n, computers, visited, i)
            answer += 1  # 모두 방문하고 빠져나오면 네트워크 +1

    return answer

def dfs(n, computers, visited, v):
    visited[v] = 1
    for i in range(n):
        if visited[i] == 0 and computers[v][i] == 1:  # 연결되어있으면
            dfs(n, computers, visited, i)