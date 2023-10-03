def solution(tickets):  # [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
    answer = []
    routes = dict()

    # 티켓 정보저장 딕셔너리 (key=출발지, value=목적지)
    for start, end in tickets:
        if start in routes:
            routes[start].append(end)
        else:
            routes[start] = [end]
    # routes : {'ICN': ['SFO', 'ATL'], 'SFO': ['ATL'], 'ATL': ['ICN', 'SFO']}

    for r in routes.keys():  # 목적지 기준 알파벳 역순으로 정렬(맨 오른쪽, 알파벳 순서상 앞에걸 pop)
        routes[r].sort(reverse=True)
    # print("routes : " + str(routes))
    # routes : {'ICN': ['SFO', 'ATL'], 'SFO': ['ATL'], 'ATL': ['SFO', 'ICN']}

    stack = ["ICN"]
    while stack:
        now = stack[-1]
        if now not in routes or len(routes[now]) == 0:  # top을 start로 하는 티켓이 없는 경우
            answer.append(stack.pop())
        else:  # 있는 경우
            stack.append(routes[now].pop())
    return answer[::-1]

# DFS(재귀이용)
def solution(tickets):
    answer = []
    visited = [False]*len(tickets)

    def dfs(start, path):
        if len(path) == len(tickets)+1:
            answer.append(path)
            return

        for idx, ticket in enumerate(tickets):
            if start == ticket[0] and visited[idx] == False:
                visited[idx] = True
                # dfs(ticket[1], path+[ticket[1]])
                dfs(ticket[1], path+[ticket[1]])
                visited[idx] = False

    dfs("ICN", ["ICN"])

    answer.sort()
    return answer[0]