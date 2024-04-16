import sys
input = sys.stdin.readline

N = int(input())
S = []
for _ in range(N):
    S.append(list(map(int, input().split())))
visited = [0 for _ in range(N)]  # 방문여부 확인
result = 1e9
answer = 0

def dfs(depth, idx):
    global result
    if depth == N//2:
        start, link = 0, 0
        for i in range(N):
            for j in range(N):
                if visited[i] and visited[j]:
                    start += S[i][j]
                elif not visited[i] and not visited[j]:
                    link += S[i][j]
        result = min(result, abs(start-link))
        return

    for i in range(idx, N):
        if not visited[i]:
            visited[i] = True
            dfs(depth+1, idx+1)  # 재귀
            visited[i] = False

dfs(0, 0)
print(result)