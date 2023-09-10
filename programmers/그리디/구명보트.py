# def solution(people, limit):
#     answer = 0
#     people.sort()  # 오름차순 정렬
#     while people:
#         if len(people) == 1:
#             answer += 1
#             break
#         if people[0] + people[-1] <= limit:
#             answer += 1
#             people.pop()
#             people.pop(0)
#         else:  # 두명의 합이 limit을 넘는 경우, 무거운 사람을 태워 보낸다
#             answer += 1
#             people.pop()
#     return answer

from collections import deque

def solution(people, limit):
    answer = 0
    queue = deque(sorted(people))
    while queue:
        if len(queue) == 1:
            answer += 1
            break
        if queue[0] + queue[-1] <= limit:
            answer += 1
            queue.popleft()
            queue.pop()
        else:  # 두명의 합이 limit을 넘는 경우, 무거운 사람을 태워 보낸다
            answer += 1
            queue.pop()
    return answer

print(solution([70, 80, 50, 50], 100))
