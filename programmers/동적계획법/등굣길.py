def solution(m, n, puddles):
    graph = [[0] * (m+1) for _ in range(n+1)]
    graph[1][1] = 1

    puddles = [[y, x] for [x, y] in puddles]

    for i in range(1, n+1):
        for j in range(1, m+1):
            if i == 1 and j == 1:
                continue
            if [i, j] in puddles:  # 웅덩이인 경우
                graph[i][j] = 0
            else:
                graph[i][j] = (graph[i-1][j] + graph[i][j-1]) % 1000000007
    return graph[n][m]

print(solution(4, 3, [[2, 2]]))


# 웅덩이 좌표말고 전체 좌표를 반대로 풀 수도 있음
def solution(m, n, puddles):
    dp = [[0] * m for _ in range(n)]
    dp[0][0] = 1

    for y in range(n):
        for x in range(m):
            if x == 0 and y == 0:
                continue
            if [x+1, y+1] in puddles:
                dp[y][x] = 0
            else:
                dp[y][x] = (dp[y-1][x] + dp[y][x-1])
    return dp[n-1][m-1] % 1000000007
