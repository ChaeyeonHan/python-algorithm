import sys
input = sys.stdin.readline

N, K = map(int, input().split())
weight = list(map(int, input().split()))

check = [0] * N
answer = 0  # 경우의 수

def dfs(count, lift):
    global answer
    if count == N:
        answer += 1
        return
    for i in range(N):
        if check[i] == 0 and lift + weight[i] - K >= 500:
            check[i] = 1
            dfs(count+1, lift+weight[i]-K)
            check[i] = 0
dfs(0, 500)
print(answer)