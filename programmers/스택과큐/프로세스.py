from collections import deque

def solution(priorities, location):  # 중요도, 순서확인하려는 인덱스 번호
    answer = []  # 앞에서 실행된 프로세스
    queue = deque((i, j) for i, j in enumerate(priorities))
    while queue:
        process = queue.popleft()
        if queue and any(process[1] < q[1] for q in queue):  # 우선순위가 더 높은값이 있다면
            queue.append(process)  # 다시 큐에 넣기
        else:
            answer.append(process)

    for i in answer:
        if i[0] == location:
            return answer.index(i)+1

print(solution([1, 1, 9, 1, 1, 1], 0))