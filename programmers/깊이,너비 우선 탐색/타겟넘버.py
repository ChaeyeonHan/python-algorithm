# BFS 풀이

from collections import deque
def solution(numbers, target):
    answer = 0
    queue = deque()
    queue.append([numbers[0], 0])  # 원소를 + 또는 - 한 값을 모두 넣어준다
    queue.append([-1*numbers[0], 0])

    while queue:
        temp, idx = queue.popleft()
        idx += 1
        if idx < len(numbers):
            queue.append([temp+numbers[idx], idx])  # 정수들의 숫자를 바꾸지 않는다
            queue.append([temp-numbers[idx], idx])
        else:
            if temp == target:
                answer += 1
    return answer


# DFS 풀이(재귀함수)
cnt = 0

def dfs(numbers, target, idx, values):  # idx : 깊이
    global cnt
    if idx == len(numbers):
        if (values == target):
            cnt += 1
            return
    else:
        dfs(numbers, target, idx + 1, values + numbers[idx])
        dfs(numbers, target, idx + 1, values - numbers[idx])


def solution(numbers, target):
    dfs(numbers, target, 0, 0)
    return cnt