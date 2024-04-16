# 대각선 체크
def diagonal(index, c):
    for i in range(index):
        if index-i == abs(c-graph[i]):  # 행과 열의 차이가 같은 경우
            return True
    return False

def dfs(idx):
    if idx == N:
        global answer
        answer += 1
        return
    for i in range(N):
        if visited[i]:  # 사용한 열이면 넘어가기
            continue
        if diagonal(idx, i):
            continue
        visited[i] = 1
        graph[idx] = i
        dfs(idx+1)
        visited[i] = 0


for i in range(1, int(input())+1):
    N = int(input())
    graph = [0 for _ in range(N)]
    visited = [0 for _ in range(N)]
    answer = 0
    dfs(0)
    print("#{} {}".format(i, answer))