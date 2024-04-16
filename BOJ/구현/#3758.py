import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N, K, T, M = map(int, input().split())
    scores = [[0] * (K+1) for _ in range(N+1)]
    attempts = [0] * (N+1)  # 제출 횟수
    last_submit = [0] * (N+1)  # 각 팀의 마지막 제출 시간

    for i in range(M):
        team, num, score = map(int, input().split())  # 팀id, 문제번호, 획득점수
        if scores[team][num] < score:
            scores[team][num] = score
        attempts[team] += 1
        last_submit[team] = (i+1)

    results = []  # 총합점수, 제출횟수, 제출시간
    for i in range(1, N+1):
        results.append([sum(scores[i]), attempts[i], last_submit[i], i])
    results.sort(key = lambda x: (-x[0], x[1], x[2]))

    for i in range(N):
        if results[i][3] == T:
            print(i+1)