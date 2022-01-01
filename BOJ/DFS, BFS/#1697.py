from collections import deque

# 현재 값과 함께 count를 넣어주기
def bfs():
    count = 0
    queue = deque()
    queue.append([N, count])

    while queue:
        x = queue.popleft()
        current = x[0]
        count = x[1]

        if visited[current] == False:
            visited[current] = True
            if current == K:
                return count
            # 그게 아니면 이동횟수 증가시키고, 모든 방향에 대해 이동시키기
            for i in (current-1, current+1, current*2):
                if 0 <= i <= 100000:
                    queue.append([i, count+1])
    return count


N, K = map(int, input().split())
visited = [False]*100001
print(bfs())