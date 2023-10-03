from collections import deque
def solution(n, edge):
    answer = 0
    queue = deque()
    route = [-1] * (n+1)  # 각 노드까지의 거리 저장
    graph = [[] for _ in range(n+1)]  # 노드 연결정보 저장

    for x in edge:
        graph[x[0]].append(x[1])
        graph[x[1]].append(x[0])

    queue.append(1)  # 1번 노드부터 시작
    route[1] = 0

    while queue:
        current = queue.popleft()
        for i in graph[current]:
            if route[i] == -1:  # 아직 방문하지 않은 노드면 큐에 추가
                queue.append(i)
                route[i] = route[current]+1  # 갱신
    max_num = max(route)
    for i in route:
        if i == max_num:
            answer += 1
    return answer

print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))