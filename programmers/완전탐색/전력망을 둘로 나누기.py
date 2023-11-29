from collections import deque

def solution(n, wires):
    graph = [[] for _ in range(n + 1)]
    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)

    def bfs(start):  # bfs로 연결된 노드 갯수 카운트
        visited = [0] * (n+1)
        q = deque([start])
        visited[start] = True
        cnt = 1

        while q:
            x = q.popleft()
            for i in graph[x]:
                if not visited[i]:
                    q.append(i)
                    visited[i] = True
                    cnt += 1
        return cnt

    answer = n
    # 전력망 끊기
    for a, b in wires:
        graph[a].remove(b)
        graph[b].remove(a)

        answer = min(abs(bfs(a)-bfs(b)), answer)
        # 원상복귀
        graph[a].append(b)
        graph[b].append(a)

    return answer